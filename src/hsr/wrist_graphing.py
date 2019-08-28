#!/usr/bin/env python
import matplotlib.pyplot as plt
from collections import deque

import rospy
from geometry_msgs.msg import WrenchStamped

class WristSensor(object):

	def __init__(self):
	
		self.topic_name = '/hsrb/wrist_wrench/raw'
		self.current_data = 0

		## Subscribe color image data from HSR
		self._image_sub = rospy.Subscriber(
		self.topic_name, WrenchStamped, self._wrist_cb)
		
		## Wait until connection
		rospy.wait_for_message(self.topic_name, WrenchStamped, timeout=5.0)


	def _wrist_cb(self, data):
		self.current_data = data.wrench.force.x
		print(data.wrench.force.x)

	def get_current_data(self):
		return self.current_data

def main():
	rospy.init_node('wrist_c')
	try:
		wrist = WristSensor()
		spin_rate = rospy.Rate(5)
		
		i = 0
		while not rospy.is_shutdown():
			plt.scatter(i, wrist.get_current_data())
			i += 1
			plt.pause(0.01)
			spin_rate.sleep()

	except rospy.ROSException as wait_for_msg_exception:
		rospy.logerr(wait_for_msg_exception)

if __name__ == "__main__" :
	main()