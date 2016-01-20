#!bin/python3
#
# picam_timestamp.py
#
# Following example at: picamera.readthedocs.org/en/release-1.10/recipes1.html#overlaying-text-on-the-output
# For the USB mount: www.raspberrypi-spi.co.uk/2014/05/how-to-mount-a-usb-flash-disk-on-the-raspberry-pi/
#
# Use omxplayer to play the video:
#     $ omxplayer python_video.h264

# TODO
# Run the video for a week and check the size
#     - save the video in smaller chunks
#         - stitch the videos together in post?
#     - convert h.264 files to mp4


import picamera as pcam
import datetime as dt

# Image parameters:
width    = 640
height   = 360
fps      = 24       # frames per second
duration = 60*60      # [s]
numberFiles = 3



# Take a video with text overlay
with pcam.PiCamera() as camera:
    camera.resolution = (width,height)
    camera.framerate = 24
    camera.start_preview()

    
    camera.annotate_background = pcam.Color('black')
    camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # camera.start_recording('/home/pi/Documents/mobile_video/python_video.h264')
    # camera.start_recording('/media/usb/python_video_usb.h264')

    for filename in camera.record_sequence('/media/usb/%d.h264' % i for i in range(1,numberFiles+1)):
        start = dt.datetime.now()
        while (dt.datetime.now() - start).seconds < duration:
            camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            camera.wait_recording(0.2)
        #camera.wait_recording(1)

    #camera.stop_recording()
    camera.stop_preview()
