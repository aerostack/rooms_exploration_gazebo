#!/usr/bin/env python3

import mission_execution_control as mxc
import time
points = [[-4.5,5,1],[5, 5, 1],[-4.8, -3.5, 1],[0, 3, 1]]

def mission():
	print("Starting mission...")
	print("Taking off...")
	mxc.executeTask('TAKE_OFF')
	mxc.startTask('FOLLOW_PATH')
	#mxc.executeTask('ROTATE', angle=90)
	time.sleep(1)
	for destination in points:
		retry = 0
		exit_status = 3
		while (retry == 0 or exit_status == 3 or exit_status == 6):
			print("Generating path to: " + str(destination))
			result = mxc.executeTask('GENERATE_PATH', destination=destination)
			print ("entra aqui")
			query = "path(?x,?y)"			
			success , unification = mxc.queryBelief(query)
			if success:				
				x = str(unification['x'])
				y = str(unification['y'])
				predicate_path = "path(" + x + "," + y + ")"
				mxc.removeBelief(predicate_path)
				predicate_object = "object(" + x + ", path)"
				mxc.removeBelief(predicate_object)
				result = eval(unification['y'])
				result = [[b for b in a ]for a in result]
				print ("Moving to"+str(result[len(result)-1]))
				print ("Path: "+str(result))
				exit_status = mxc.executeTask('SEND_PATH', path = result, speed = 0.4, yaw_mode = 0)[1]
				print (exit_status)
				retry = 1
	print (exit_status)
	mxc.executeTask('LAND')
	mxc.startTask('SAVE_OCCUPANCY_GRID', map_name="$APPLICATION_PATH/maps/planta")
	print('Finish mission...')
