#Main code to run sequentially
# import camera_run as cr
import sun_detection as sd

# print("Calling camera-test to take 4 images")
# cr.CaptureImages(preview=True, num_pics=4)

# print("Calling camera-test to take 4 seconds video")
# cr.CaptureVideo(preview=True, num_secs=4)

print("Calling Sun_detection Algorithm with captured images")
sd.SunDetection();