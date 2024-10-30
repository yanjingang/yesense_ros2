1. 测试环境说明
基于Ubuntu 22.04.4 LTS/Humble、Ubuntu 20.04.4 LTS/Foxy、Ubuntu 20.04.4 LTS/Rolling版本测试

2. 在**项目根目录下**打开终端，执行 `chmod +x *.sh` 为项目下的脚本增加可执行权限

3. set serial library path
在项目根目录下打开终端，依次输入执行以下命令
sudo sh -c "echo '$(pwd)/install/yesense_std_ros2/lib/yesense_std_ros2/serial' >> /etc/ld.so.conf"
sudo ldconfig

4. 生成msg消息头文件
在项目根目录下打开终端，输入执行以下命令  './gen_interface.sh' 或  'colcon build --packages-select yesense_interface'
（在更改msg消息格式时需重新编译）或着把该命令添加到build.sh脚本中

5. build package
- 在**项目根目录下**打开终端，执行 `./build.sh` 编译整个项目
- 在Foxy版本下会编译出错，需要将yesense_node.cpp源文件中把407行代码注释掉，使用404行的代码
 
6. run
- 默认配置为：设备 '/dev/ttyUSB0' 、波特率为460800， 使用ROS串口驱动
- 在项目根目录下打开终端，输入 `./run.sh` 或 './run_with_launch.sh' 并执行，如果始终打不开串口或为了确保可以正常打开串口，
则需要添加权限，使用命令 sudo chmod 777 /dev/ttyUSBx，其中ttyUSBx为实际的串口号
使用 './run.sh' 时，如需要修改设备端口或波特率时，则需要修改源码，然后重新编译
使用 './run_with_launch.sh' 时，如果实际情况与默认值不相同的情况下，
则需要修改在 ‘/src/yesense_std_ros2/config’ 目录下 'yesense_config.yaml' 配置文件，
其中driver_type的值为 ‘ros_serial’ 和 'linux_serial' 之一，
波特率目前支持9600, 19200, 38400, 57600, 115200, 230400, 460800, 921600

- 在项目根目录下打开终端，执行 `ros2 topic echo /imu_data` (需确保先设置了环境变量 '. install/setup.bash')可查看器件输出的原始数据

7. 支持的topic
### ros 内置 topic

/sensor_msgs/msg/Imu            : 加速度、角速度、四元数
/visualization_msgs/msg/Marker  : 姿态，定位，形状数据（用于 rviz 可视化） 
/geometry_msgs/msg/Pose         : 传感器姿态数据 

### yesense 扩展 topic
/imu_data       ：imu数据，包含tid、加速度、角速度、传感器温度、采样时间戳
/sensor_10axis  : 10轴数据，包含tid、加速度、角速度、传感器温度、采样时间戳、磁场强度(原始数据和归一化数据)、气压（保留）

/euler_only     : 欧拉角数据，包括tid、横滚角、俯仰角、航向角
/robot_lord     : 机器人LORD格式数据，包括tid、加速度、角速度、四元数
/att_min_vru    : 推荐的姿态传感器VRU模式最小数据，包含tid、加速度、角速度、传感器温度、采样时间戳、欧拉角
/att_min_ahrs   : 推荐的姿态传感器AHRS模式最小数据，包含tid、加速度、角速度、磁场强度（原始数据和归一化数据）、传感器温度、采样时间戳、欧拉角
/att_all        : 姿态产品所有数据，包含tid、加速度、角速度、磁场强度（原始数据和归一化数据）、传感器温度、采样时间戳、欧拉角、四元数

/pos_only       : 位置数据，包括tid、经纬高、组合状态
/nav_min        : 推荐的组合导航产品的最小数据，包含tid、欧拉角、经纬高、组合状态
/nav_min_utc    : 推荐的组合导航产品的带UTC时间的最小数据，包含tid、欧拉角、经纬高、UTC时间、组合状态
/nav_all        : 组合导航所有的数据，包含tid、加速度、角速度、欧拉角、四元数、传感器温度、位置、组合状态、enu速度、utc时间、气压（保留）

8. 订阅者示例
- 在项目根目录下打开终端，输入 `ros2 run yesense_std_ros2 yesense_node_subscriber` 并执行（如果使用了新的终端，请先执行 `. install/setup.bash`命令）   
