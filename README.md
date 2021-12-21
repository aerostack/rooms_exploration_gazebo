# Application: rooms_exploration_gazebo

This application illustrates how a drone explores a room in px4 simulator using ROS Noetic. During the mission execution, it is possible to pause and continue the mission execution. While the mission is executing, the drone starts mapping the room while generating paths in order to explore it.

In order to execute the mission, perform the following steps:

- Install Lidar components:

        $ ./lidar_installation.sh

- Execute the script that launches Gazebo for this project:

        $ ./launcher_gazebo.sh


- Wait until the following window is presented:

<img src="https://github.com/aerostack/rooms_exploration_gazebo/blob/devel/doc/gazeborooms.png" width=600>

- Execute the script that launches the Aerostack components for this project:

        $ ./main_launcher.sh

As a result of this command, a set of windows are presented to monitor the execution of the mission. These windows include:
- Lidar mapping
- Executed nodes

In order to start the execution of the mission, execute the following command:

	$ rosservice call /drone111/python_based_mission_interpreter_process/start

The following video illustrates how to launch the project:

[ ![Launch](https://i.ibb.co/0Y6y5Rb/Captura-de-pantalla-de-2021-10-12-23-31-24.png)](https://youtu.be/2SUIx0qxNNY)

The following video shows the complete execution:

[ ![Execution](https://i.ibb.co/Qcb0Zby/Captura-de-pantalla-de-2021-10-12-23-31-51.png)](https://youtu.be/qGbNzYkE19U)


