#!/usr/bin/env python
"""Camera image collection"""

import cv2
from cv_bridge import CvBridge, CvBridgeError

import rospy
from sensor_msgs.msg import Image


class ImgCapture(object):
    """color detection class using OpenCV"""

    STEREO_L = '/hsrb/head_l_stereo_camera/image_rect_color'
    STEREO_R = '/hsrb/head_r_stereo_camera/image_rect_color'
    RGB_D    = '/hsrb/head_rgbd_sensor/rgb/image_rect_color'
    HAND_CAM = '/hsrb/hand_camera/image_raw'

    def __init__(self):
        self._bridge = CvBridge()
        self._input_image = None
        self.topic_name = self.RGB_D

        # # Subscribe color image data from HSR
        self._image_sub = rospy.Subscriber(
            self.topic_name, Image, self._color_image_cb)
        # # Wait until connection
        rospy.wait_for_message(self.topic_name, Image, timeout=5.0)

    def set_current_mode(self,mode):
        self._image_sub.unregister()
        if mode == self.STEREO_L :
            self._image_sub = rospy.Subscriber(
            self.STEREO_L, Image, self._color_image_cb)
            # rospy.wait_for_message(self.STEREO_L, Image, timeout=5.0)
            print("Mode : STEREO_L")

        if mode == self.STEREO_R :
            self._image_sub = rospy.Subscriber(
            self.STEREO_R, Image, self._color_image_cb)
            # rospy.wait_for_message(self.STEREO_R, Image, timeout=5.0)
            print("Mode : STEREO_R")

        if mode == self.RGB_D :
            self._image_sub = rospy.Subscriber(
            self.RGB_D, Image, self._color_image_cb)
            # rospy.wait_for_message(self.RGB_D, Image, timeout=5.0)
            print("Mode : RGB_D")

        if mode == self.HAND_CAM :
            self._image_sub = rospy.Subscriber(
            self.HAND_CAM, Image, self._color_image_cb)
            # rospy.wait_for_message(self.HAND_CAM, Image, timeout=5.0)
            print("Mode : HAND_CAM")

    def _color_image_cb(self, data):
        try:
            self._input_image = self._bridge.imgmsg_to_cv2(data, "bgr8")
        except CvBridgeError as cv_bridge_exception:
            rospy.logerr(cv_bridge_exception)

    def extract_image(self):
        return self._input_image

def main():
    rospy.init_node('image_capture')
    try:
        img_capture = ImgCapture()
        spin_rate = rospy.Rate(30)

        # UpdateGUI Window
        while not rospy.is_shutdown():
            
            if cv2.waitKey(5) == 49 :
                img_capture.set_current_mode(ImgCapture.STEREO_L)

            elif cv2.waitKey(5) == 50 :
                img_capture.set_current_mode(ImgCapture.STEREO_R)

            elif cv2.waitKey(5) == 51 :
                img_capture.set_current_mode(ImgCapture.RGB_D)

            elif cv2.waitKey(5) == 52 :
                img_capture.set_current_mode(ImgCapture.HAND_CAM)

            dst_image = img_capture.extract_image()
            cv2.imshow("Color Detection Image Window", dst_image)
                
            cv2.waitKey(3)
            spin_rate.sleep()

    except rospy.ROSException as wait_for_msg_exception:
        rospy.logerr(wait_for_msg_exception)

    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()



