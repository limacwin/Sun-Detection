#Main code to run sequentially
import camera_run as cr
import sun_detection as sd
import dual_motors_rotation as dmr
import time

print("Sleeping for 10s..")
time.sleep(10)

print("Calling camera-test to take 1 images")
offsetX, offsetY = cr.CaptureImages(preview=True, num_pics=1)

dmr.unitsConversion(offsetX, offsetY)

# print("Calling camera-test to take 4 seconds video")
# cr.CaptureVideo(preview=True, num_secs=4)

# print("Calling Sun_detection Algorithm with captured images")
# sd.SunDetection();