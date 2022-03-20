# main code to run sequentially
import camera_run as cr
import dual_motors_rotation as dmr
import time

print("Sleeping for 10s..")
time.sleep(10)

# these times will be fetched from the weather forecast api
sunriseTime = 7
sunsetTime = 17
timeDuration = sunsetTime - sunriseTime 

start = time.time()
end = time.time()

while(end - start <= timeDuration):
    print("Calling camera-test to take 1 images")
    offsetX, offsetY = cr.CaptureImages(preview=True)

    dmr.unitsConversion(offsetX, offsetY)

    end = time.time()