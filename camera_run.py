from picamera import PiCamera
from time import sleep
import sun_detection as sd

def CaptureImages(preview):
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.rotation = 180

    # code to capture images
    if(preview):
        camera.start_preview()

    sleep(5) # in seconds, sleep to give the sensor some time to capture the light levels (min=3s)
    camera.capture('images/captured_image.jpg')
    sleep(2)
    camera.stop_preview()
    offsetX, offsetY = sd.SunDetection("images/captured_image.jpg")

    return offsetX, offsetY

# def CaptureVideo(preview, num_secs):
#     # code to record video for 'num_sec' seconds
#     if(preview):
#         camera.start_preview()
#     camera.start_recording('videos/test_video.h264')
#     sleep(num_secs)
#     if(preview):
#         camera.stop_preview()
#     camera.stop_recording()
    