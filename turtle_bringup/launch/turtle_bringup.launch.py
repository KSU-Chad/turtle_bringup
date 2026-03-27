# turtle_bringup.launch.py
#
# WHAT THIS DOES:
#   Starts the full turtlesim system with a single command:
#     - turtlesim_node  (blue background, configured via parameters)
#     - turtle_teleop_key  (opens in its own xterm window automatically)
#
# USAGE:
#   ros2 launch turtle_bringup turtle_bringup.launch.py
#
# PREREQUISITES:
#   sudo apt install xterm
#
# WHY A PACKAGE?
#   Instead of opening two terminals and running two commands, this package
#   lets anyone launch the complete turtlesim system with one command from
#   anywhere on the system — no need to know where the launch file lives.

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        # --- Node 1: turtlesim simulator ---
        # Parameters override the default grey background with blue.
        # These are the same parameters you can inspect with:
        #   ros2 param list /sim
        #   ros2 param get /sim background_r
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',                  # overrides default node name '/turtlesim'
            parameters=[{
                'background_r': 0,
                'background_g': 0,
                'background_b': 255,
            }]
        ),

        # --- Node 2: keyboard teleop ---
        # prefix='xterm -e' opens a new terminal window for this node.
        # This is necessary because turtle_teleop_key needs keyboard focus —
        # it can't receive keystrokes from the same terminal running ros2 launch.
        #
        # Try removing prefix and observe what happens (teleop starts but
        # arrow keys don't work — great discussion point for class).
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',               # overrides default node name '/teleop_turtle'
            prefix='xterm -e',
        ),

    ])
