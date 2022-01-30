from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 180
def CaptureImages(preview, num_pics):
    # code to capture images
    if(preview):
        camera.start_preview()

    for i in range(num_pics):
        sleep(4) # in seconds, sleep to give the sensor some time to capture the light levels (min=3s)
        camera.capture('images/test_image_%s.jpg' %i)
        sleep(2)
    if(preview):
        camera.stop_preview()

def CaptureVideo(preview, num_secs):
    # code to record video for 'num_sec' seconds
    if(preview):
        camera.start_preview()
    camera.start_recording('videos/test_video.h264')
    sleep(num_secs)
    if(preview):
        camera.stop_preview()
    camera.stop_recording()
    