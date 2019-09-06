#!/usr/bin/env python
import matplotlib.pyplot as plt
from collections import deque

import rospy
from geometry_msgs.msg import WrenchStamped


class WristSensor(object):

	def __init__(self):
	
		self.topic_name = '/hsrb/wrist_wrench/raw'

		## Subscribe color image data from HSR
		self._image_sub = rospy.Subscriber(
		self.topic_name, WrenchStamped, self._wrist_cb)
		
		## Wait until connection
		rospy.wait_for_message(self.topic_name, WrenchStamped, timeout=5.0)


	def _wrist_cb(self, data):
		print(data.wrench.force.x)

def main():
	rospy.init_node('wrist_c')
	try:
		wrist = WristSensor()
		spin_rate = rospy.Rate(30)

		while not rospy.is_shutdown():
			spin_rate.sleep()

	except rospy.ROSException as wait_for_msg_exception:
		rospy.logerr(wait_for_msg_exception)

if __name__ == "__main__" :
	main()

