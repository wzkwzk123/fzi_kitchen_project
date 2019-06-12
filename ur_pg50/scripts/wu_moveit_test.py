#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, sys
import moveit_commander
from moveit_msgs.msg import RobotTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint

from geometry_msgs.msg import PoseStamped, Pose
from tf.transformations import euler_from_quaternion, quaternion_from_euler

class MoveItIkDemo:
    def __init__(self):
        moveit_commander.roscpp_initialize(sys.argv)
        
        rospy.init_node('moveit_ik_demo')

        arm = moveit_commander.MoveGroupCommander('arm')
                
        
        arm.set_named_target('home1')
        arm.go()
        rospy.sleep(0.5)


        arm.set_named_target('home2')
        arm.go()
                

                
        


            
        
           
        

        # 关闭并退出moveit
        moveit_commander.roscpp_shutdown()
        moveit_commander.os._exit(0)

if __name__ == "__main__":
    MoveItIkDemo()

    
    
