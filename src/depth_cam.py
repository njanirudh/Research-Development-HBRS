
'''
Created on 19Jun2015
Stream depth video using openni2 opencv-python (cv2)
Requires the following libraries:
    1. OpenNI-Linux-<Platform>-2.2 <Library and driver>
    2. primesense-2.2.0.30 <python bindings>
    3. Python 3.X
    4. OpenCV 4.X
Current features:
    1. Convert primensense oni -> numpy
    2. Stream and display depth
    3. Keyboard commands
        press esc to exit
        press s to save current screen and distance-map
NOTE:
    1. On device streams:  IR and RGB streams do not work together
       Depth & IR  = OK
       Depth & RGB = OK
       RGB & IR    = NOT OK
    2. Do not synchronize with rgb or stream will freeze
@author: Anirudh NJ
'''

import numpy as np
import cv2
from openni import openni2
from openni import _openni2 as c_api

## Path of the OpenNI redistribution OpenNI2.so or OpenNI2.dll
# Windows
# dist = 'C:\Program Files\OpenNI2\Redist\OpenNI2.dll'
# OMAP
# dist = '/home/carlos/Install/kinect/OpenNI2-Linux-ARM-2.2/Redist/'
# Linux
dist = '/home/anirudh/SDK/cpp/OpenNI2/OpenNI-Linux-x64-2.2/Redist'

## Initialize openni and check
openni2.initialize(dist)
if (openni2.is_initialized()):
    print("openNI2 initialized")
else:
    print("openNI2 not initialized")


dev = openni2.Device.open_any()
print ('Some Device Information')
print (dev.get_sensor_info(openni2.SENSOR_DEPTH))
print (dev.get_sensor_info(openni2.SENSOR_IR))
print (dev.get_sensor_info(openni2.SENSOR_COLOR))

## streams
# Depth stream
depth_stream = dev.create_depth_stream()

# IR stream
ir_stream = dev.create_ir_stream()

## Set stream speed and resolution
width  = 640
height = 480
fps    = 30

## Set the video properties
#print 'Get b4 video mode', depth_stream.get_video_mode()
depth_stream.set_video_mode(c_api.OniVideoMode(pixelFormat=c_api.OniPixelFormat.ONI_PIXEL_FORMAT_DEPTH_1_MM,
                                               resolutionX=width, resolutionY=height, fps=fps))
#print 'Get after video mode', depth_stream.get_video_mode()

## Start the streams
depth_stream.start()
ir_stream.start()


def get_depth1():
    """
    Returns numpy ndarrays representing raw and ranged depth images.
    Outputs:
        depth:= raw depth, 1L ndarray, dtype=uint16, min=0, max=2**12-1
        d4d  := depth for dislay, 3L ndarray, dtype=uint8, min=0, max=255
    Note1:
        fromstring is faster than asarray or frombuffer
    Note2:
        depth = depth.reshape(120,160) #smaller image for faster response
                NEEDS default video configuration
        depth = depth.reshape(240,320) # Used to MATCH RGB Image (OMAP/ARM)
    """
    depth_frame = depth_stream.read_frame()
    depth = np.fromstring(depth_frame().get_buffer_as_uint16(),dtype=np.uint16).reshape(height,width)  # Works & It's FAST
    d4d = np.uint8(depth.astype(float) *255/ 2**12-1) # Correct the range. Depth images are 12bits
    #d4d = cv2.cvtColor(d4d,cv2.COLOR_GRAY2RGB)
    d4d = np.dstack((d4d,d4d,d4d)) # faster than cv2 conversion
    return depth, d4d
#get_depth


def get_depth():
    """
    Returns numpy ndarrays representing the raw and ranged depth images.
    Outputs:
        dmap:= distancemap in mm, 1L ndarray, dtype=uint16, min=0, max=2**12-1
        d4d := depth for dislay, 3L ndarray, dtype=uint8, min=0, max=255
    Note1:
        fromstring is faster than asarray or frombuffer
    Note2:
        .reshape(120,160) #smaller image for faster response
                OMAP/ARM default video configuration
        .reshape(240,320) # Used to MATCH RGB Image (OMAP/ARM)
                Requires .set_video_mode
    """
    dmap = np.fromstring(depth_stream.read_frame().get_buffer_as_uint16(),dtype=np.uint16).reshape(height,width)  # Works & It's FAST
    d4d = np.uint8(depth.astype(float) *255/ 2**12-1) # Correct the range. Depth images are 12bits
    #d4d = cv2.cvtColor(d4d,cv2.COLOR_GRAY2RGB)
    d4d = np.dstack((d4d,d4d,d4d)) # faster than cv2 conversion
    return dmap, d4d
#get_depth

def get_ir():
    """
    Returns numpy ndarrays representing raw and ranged infra-red(IR) images.
    Outputs:
        ir    := raw IR, 1L ndarray, dtype=uint16, min=0, max=2**12-1
        ir4d  := IR for display, 3L ndarray, dtype=uint8, min=0, max=255
    """
    ir_frame = ir_stream.read_frame()
    ir_frame_data = ir_stream.read_frame().get_buffer_as_uint16()
    ir4d = np.ndarray((ir_frame.height, ir_frame.width),dtype=np.uint16, buffer = ir_frame_data).astype(np.float32)
    ir4d = np.uint8((ir4d/ir4d.max()) * 255)
    ir4d = cv2.cvtColor(ir4d,cv2.COLOR_GRAY2RGB)
    return ir_frame, ir4d
#get_ir

frame_idx = 0

## main loop
done = False
while not done:
    key = cv2.waitKey(1)
    if (key&255) == 27:
        done = True
    ## Read in the streams
    # Depth
    _,d4d = get_depth()
    # Infrared
    _, ir4d = get_ir()
    cv2.imshow("Depth||IR", np.hstack((d4d, ir4d)))
    frame_idx+=1
# end while

## Release resources and terminate
cv2.destroyAllWindows()
depth_stream.stop()
openni2.unload()
print ("Terminated")