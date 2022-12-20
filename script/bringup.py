#!/usr/bin/env python
##############################################################################
# Imports
##############################################################################
import rospy
from std_msgs.msg import Empty, Bool
from geometry_msgs.msg import PoseStamped

goal_pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=10)

def on_start(msg):
    rospy.loginfo("Started")
    goal = PoseStamped()
    goal.header.frame_id = "map"
    goal.pose.position.x = 0
    goal.pose.position.y = 0
    goal.pose.position.z = 0
    goal.pose.orientation.x = 0
    goal.pose.orientation.y = 0
    goal.pose.orientation.z = 0
    goal.pose.orientation.w = 1
    goal_pub.publish(goal)

def on_finish(msg):
    rospy.loginfo("Finished")

rospy.Subscriber('/start', Empty, on_start)
rospy.Subscriber('/finish', Bool, on_finish)

##############################################################################
# Main
##############################################################################
if __name__ == '__main__':
    rospy.init_node("bringup")
    rospy.loginfo("Initialized")
    rospy.spin()
