#!/usr/bin/env python
# coding: utf-8
import rospy
from geometry_msgs.msg import Twist
#【OS】Ubuntu 16.04.5 LTS
#【ROS version】kinetic
#このプログラムを実行することでROSで動かせるロボットTurtleBotを強制的に停止(もしくは指定した速度で移動)させられます。尚、これを実行する前に以下の３つを予め実行しておくこと。
#rosrun rviz rviz
#roslaunch turtlebot_gazebo turtlebot_world.launch
#roslaunch turtlebot_gazebo amcl_demo.launch

def main():
    pub=rospy.Publisher("/mobile_base/commands/velocity",Twist,queue_size=10)
    vel_msg=Twist()
    vel_msg.linear.x=0
    vel_msg.linear.y=0
    vel_msg.linear.z=0
    vel_msg.angular.x=0
    vel_msg.angular.y=0
    vel_msg.angular.z=0
    while True :
        pub.publish(vel_msg)

    rospy.spin()

if __name__== "__main__":
    try:
        rospy.init_node("SetVelocity")
        main()
    except rospy.ROSInterruptException:
        pass

