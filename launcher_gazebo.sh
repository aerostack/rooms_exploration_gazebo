#!/bin/bash

DRONE_SWARM_MEMBERS=$1
export APLICATION_PATH=${PWD}
MAV_NAME=hummingbird_laser

if [ -z $DRONE_SWARM_MEMBERS ] # Check if NUMID_DRONE is NULL
  then
    #Argument 1 empty
      echo "-Setting Swarm Members = 1"
      DRONE_SWARM_MEMBERS=1
  else
      echo "-Setting DroneSwarm Members = $1"
fi

gnome-terminal  \
    --tab --title "DroneRotorsSimulator" --command "bash -c \"
roslaunch ${APLICATION_PATH}/configs/gazebo_files/launch/env_mav_rl_navigation.launch project:=${APLICATION_PATH} world_name:=lidar_example;
            exec bash\""  &

for (( c=1; c<=$DRONE_SWARM_MEMBERS; c++ )) 
do  
  gnome-terminal  \
  --tab --title "Spawn_mav" --command "bash -c \"
  roslaunch rotors_gazebo mav_swarm_rl_navigation.launch --wait \
    namespace:=$MAV_NAME$c \
    mav_name:=$MAV_NAME \
    log_file:=$MAV_NAME$c \
    x:=0 \
    y:=0;
  exec bash\""  &
done

