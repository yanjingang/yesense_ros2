
import launch
import launch_ros.actions
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    config = os.path.join(
        get_package_share_directory('yesense_std_ros2'),
        'config',
        'yesense_config.yaml',
    )

    rviz_file = os.path.join(
            get_package_share_directory('yesense_std_ros2'),
            'rviz',
            'imu.rviz')

    rviz = launch_ros.actions.Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', launch.substitutions.LaunchConfiguration(
                        'rviz_param_dir',
                        default=rviz_file)]
        )

    return LaunchDescription([
         Node(
            package='yesense_std_ros2',
            executable='yesense_node_publisher',
            name='yesense_pub',
            parameters=[config],
            output='screen',
            ),
            rviz
        ])
