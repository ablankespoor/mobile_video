#!bin/python3
#
# picam_test.py
#
# Following tutorial at: https://www.raspberrypi.org/learning/python-picamera-setup/worksheet.md
#
# Use omxplayer to play the video:
#     $ omxplayer python_video.h264

# TODO
# Run the video for a week and check the size
#     - save this to USB?
#     - save the video in smaller chunks
#     - open and view the video from another computer

import time
import picamera



### Take a snapshot
##with picamera.PiCamera() as camera:
##    camera.start_preview()
##    time.sleep(5)
##    camera.capture('/home/pi/Documents/mobile_video/python_image_test.jpg')
##    camera.stop_preview()

# Take a video
with picamera.PiCamera() as camera:
    camera.resolution = (640,360)
    camera.framerate = 24
    camera.start_preview()
    camera.start_recording('/home/pi/Documents/mobile_video/python_video.h264')
    camera.wait_recording(60)
    camera.stop_recording()
    camera.stop_preview()
