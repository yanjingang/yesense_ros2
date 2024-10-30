#!/bin/bash

echo "start colcon build shell"

# build cmd
#colcon build --packages-select yesense_interface
colcon build --packages-select yesense_std_ros2
