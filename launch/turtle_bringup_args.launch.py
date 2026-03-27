# turtle_bringup_args.launch.py
#
# WHAT THIS DOES:
#   Same as turtle_bringup.launch.py, but exposes background color as
#   command-line arguments so the user can configure them at launch time.
#
# USAGE (defaults — same blue background as turtle_bringup.launch.py):
#   ros2 launch turtle_bringup turtle_bringup_args.launch.py
#
# USAGE (custom colors — try these in class):
#   ros2 launch turtle_bringup turtle_bringup_args.launch.py bg_r:=255 bg_g:=0 bg_b:=0
#   ros2 launch turtle_bringup turtle_bringup_args.launch.py bg_r:=0 bg_g:=200 bg_b:=0
#   ros2 launch turtle_bringup turtle_bringup_args.launch.py bg_r:=255 bg_g:=165 bg_b:=0
#
# LIST AVAILABLE ARGUMENTS without launching:
#   ros2 launch turtle_bringup turtle_bringup_args.launch.py --show-args
#
# KEY CONCEPTS INTRODUCED:
#   - DeclareLaunchArgument  — declares a named argument with default + description
#   - LaunchConfiguration    — reads the argument's value at launch time
#   - substitutions          — LaunchConfiguration is evaluated lazily, not at import time

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    # --- Declare launch arguments ---
    # Each argument has a name, default value, and description.
    # The description shows up when the user runs --show-args.
    bg_r_arg = DeclareLaunchArgument(
        'bg_r',
        default_value='0',
        description='Background red channel (0-255)'
    )

    bg_g_arg = DeclareLaunchArgument(
        'bg_g',
        default_value='0',
        description='Background green channel (0-255)'
    )

    bg_b_arg = DeclareLaunchArgument(
        'bg_b',
        default_value='255',
        description='Background blue channel (0-255)'
    )

    # --- Read argument values via LaunchConfiguration ---
    # LaunchConfiguration is a substitution — it reads the argument value
    # at launch time, after the user has had a chance to override defaults.
    # Important: you cannot print() or inspect these at import time —
    # they are evaluated lazily by the launch framework.
    bg_r = LaunchConfiguration('bg_r')
    bg_g = LaunchConfiguration('bg_g')
    bg_b = LaunchConfiguration('bg_b')

    # --- Nodes ---
    sim_node = Node(
        package='turtlesim',
        executable='turtlesim_node',
        name='sim',
        parameters=[{
            'background_r': bg_r,
            'background_g': bg_g,
            'background_b': bg_b,
        }]
    )

    teleop_node = Node(
        package='turtlesim',
        executable='turtle_teleop_key',
        name='teleop',
        prefix='xterm -e',
    )

    # --- Assemble the LaunchDescription ---
    # Arguments MUST be listed before the nodes that use them.
    return LaunchDescription([
        bg_r_arg,
        bg_g_arg,
        bg_b_arg,
        sim_node,
        teleop_node,
    ])
