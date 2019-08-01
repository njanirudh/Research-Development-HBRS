import cv2
import numpy as np
import cv2.aruco as aruco

class ArucoMeasurement:

    def __init__(self, length :int):
        """

        :param length: Length of a side of the Aruco marker
        """
        self.__aruco_length = length
        self.__conversion_ratio = None

        self.__cam_mat = None
        self.__dist_mat = None

        self.__aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)
        self.__parameters = aruco.DetectorParameters_create()

        # Setting the debug visualization boolean
        self.DEBUG_DRAW = True

    def set_calibration_path(self,path:str):
        self.__cam_mat = None
        self.__dist_mat = None

    def set_calibration_image(self, image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # lists of ids and the corners belonging to each id
        corner_pnts, ids, rejectedImgPoints = aruco.detectMarkers(gray, self.__aruco_dict,
                                                                       parameters=self.__parameters)

        if np.all(ids != None):
            for i in range(len(ids)):
                # Estimate pose of each marker and return the values rvet and tvec-different from camera coefficients
                self.__r_vec, self.__t_vec, _ = aruco.estimatePoseSingleMarkers(corner_pnts[i], 0.05,
                                                                                self.__cam_mat,
                                                                                self.__dist_mat)

                if (self.DEBUG_DRAW == True):
                    aruco.drawAxis(image, self.__cam_mat, self.__dist_mat, self.__r_vec[0], self.__t_vec[0],
                                   0.05)  # Draw Axis
                    aruco.drawDetectedMarkers(image, corner_pnts)  # Draw A square around the markers

            cv2.putText(image, "Id: " + str(ids), (0, 64), cv2.FONT_HERSHEY_SIMPLEX
                        , 1, (0, 255, 0), 2, cv2.LINE_AA)


    def get_distance_from_image(self,image):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # lists of ids and the corners belonging to each id
        corner_pnts, ids, rejectedImgPoints = aruco.detectMarkers(gray, self.__aruco_dict,
                                                                       parameters=self.__parameters)

        if np.all(ids != None):
            for i in range(len(ids)):
                # Estimate pose of each marker and return the values rvet and tvec-different from camera coefficients
                self.__r_vec, self.__t_vec, _ = aruco.estimatePoseSingleMarkers(corner_pnts[i], 0.05,
                                                                                self.__cam_mat,
                                                                                self.__dist_mat)

                if (self.DEBUG_DRAW == True):
                    aruco.drawAxis(image, self.__cam_mat, self.__dist_mat, self.__r_vec[0], self.__t_vec[0],
                                   0.05)  # Draw Axis
                    aruco.drawDetectedMarkers(image, corner_pnts)  # Draw A square around the markers

            cv2.putText(image, "Id: " + str(ids), (0, 64), cv2.FONT_HERSHEY_SIMPLEX
                        , 1, (0, 255, 0), 2, cv2.LINE_AA)


if __name__ == "__main__":

    distance_measure = ArucoMeasurement(40)