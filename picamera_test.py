#picamera_test.py
import picamera
import time

path = "/home/pi/src6/06_multimedia"

camera = picamera.PiCamera()

try:
    camera.resolution = (640, 480) #사진크기
    camera.start_preview()
    time.sleep(3) #카메라 촬영 준비시간 필요
    camera.rotation = 180
    #camera.capture("%s/photo.jpg" % path) #사진촬영

    camera.start_recording("%s/video.h264" % path) # 동영상 촬영
    #time.sleep(10)
    input("press enter to stop")
    camera.stop_recording()

finally:
    camera.stop_preview()