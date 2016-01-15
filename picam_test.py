import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(5)
    camera.capture('/home/pi/Documents/mobile_video/python_image_test.jpg')
    camera.stop_preview()
