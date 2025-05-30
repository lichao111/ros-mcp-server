#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def callback(msg):
    rospy.loginfo(f"Received /cmd_vel: linear={msg.linear}, angular={msg.angular}")

def main():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber('/cmd_vel', Twist, callback)
    rospy.loginfo("Listening to /cmd_vel...")
    rospy.spin()

if __name__ == '__main__':
    main()