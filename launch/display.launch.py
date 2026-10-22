from ament_index_python.packages import get_package_share_directory
import os
import xacro
from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():

    #preparing paths
    pkg_path=get_package_share_directory("my_bot_description")
    xacro_file=os.path.join(pkg_path, "urdf", "my_bot.urdf.xacro")

    #compiling xacro file into raw xml file
    robot_description_raw=xacro.process_file(xacro_file).toxml()

    #Declaring Nodes to run
    robot_state_publisher_node=Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": robot_description_raw}]
    )

    robot_joints_state_publisher_gui_node=Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        output="screen"
    )

    #preparing rviz configuration path
    rviz_file=os.path.join(pkg_path,"rviz","my_bot.rviz")
    rviz_node=Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        arguments=["--display-config", rviz_file]
    )

    return LaunchDescription([
        robot_state_publisher_node,
        robot_joints_state_publisher_gui_node,
        rviz_node
    ])
