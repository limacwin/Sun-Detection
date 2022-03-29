# main code to run sequentially
import camera_run as cr
import dual_motors_rotation as dmr
import time

def main():
    print("Sleeping for 10s..")
    time.sleep(10)

    # these times will be fetched from the weather forecast api
    sunriseTime = 7
    sunsetTime = 17
    timeDuration = sunsetTime - sunriseTime # 10s
    timeDuration = 3600

    start = time.time()
    end = time.time()

    while(end - start <= timeDuration):
        # print("Calling camera-test to take 1 images")
        offsetX, offsetY = cr.CaptureImages(preview=False)

        dmr.unitsConversion(offsetX, offsetY)

        end = time.time()