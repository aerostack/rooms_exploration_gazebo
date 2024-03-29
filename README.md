# Application: rooms_exploration_gazebo

This application illustrates how a drone explores a room in px4 simulator using ROS Noetic. During the mission execution, it is possible to pause and continue the mission execution. While the mission is executing, the drone starts mapping the room while generating paths in order to explore it.

In order to execute the mission, perform the following steps:

- Install package Hector_Slam, Move_base and Amcl if not installed yet:
```
$ sudo apt install ros-noetic-hector-slam
$ sudo apt install ros-noetic-move-base
$ sudo apt install ros-noetic-amcl 
```

- Install Lidar components:

        $ ./lidar_installation.sh

- Execute the script that launches Gazebo for this project:

        $ ./launch_gazebo.sh


- Wait until the following window is presented:

<img src="https://github.com/aerostack/rooms_exploration_gazebo/blob/v5-libeccio/doc/gazeborooms.png" width=600>

- Execute the script that launches the Aerostack components for this project:

        $ ./df_main_launcher.sh

As a result of this command, a set of windows are presented to monitor the execution of the mission. These windows include:
- Lidar mapping
- Executed nodes

In order to start the execution of the mission, execute the following command:

	$ rosservice call /drone1/python_based_mission_interpreter_process/start

The following video illustrates how to launch the project:

[ ![Launch](https://github.com/aerostack/rooms_exploration_gazebo/blob/v5-libeccio/doc/launch_rooms.png)](https://youtu.be/2SUIx0qxNNY)

The following video shows the complete execution:

[ ![Execution](https://github.com/aerostack/rooms_exploration_gazebo/blob/v5-libeccio/doc/execute_rooms.png)](https://youtu.be/qGbNzYkE19U)


