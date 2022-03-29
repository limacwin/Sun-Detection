import RPi.GPIO as GPIO
import time

in1 = 24
in2 = 23
in3 = 4
in4 = 22
en1 = 25
en2 = 27
temp1 = 1
temp2 = 1

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1 = GPIO.PWM(en1,1000)

GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2 = GPIO.PWM(en2,1000)

p1.start(25)
p2.start(27)
p1.ChangeDutyCycle(100)
p2.ChangeDutyCycle(100)

full_rotation_time = 10 # to be changed later

def unitsConversion(offsetX, offsetY):
    mmUnits = 0.264583333
    offsetX = offsetX * mmUnits
    offsetY = offsetY * mmUnits

    # Total distance covered by upper gearbox motor: 2*Pi*r, where r = 22.5mm, circumference = 141.372mm
    # Hence, since the motors move at 3RPM speed, total distance covered in 60s = 141.372 * 3 = 424.1160mm
    # Therefore, in 1s, 7.0686mm will be covered (424.1160 / 60)
    # To get the amount of time (in seconds) the motors should move, time = (offset / 7.0686)

    distancePerSecond = 7.0686
    offsetXTime = offsetX / distancePerSecond
    offsetYTime = offsetY / distancePerSecond

    motorRotation(offsetXTime, offsetYTime)

def motorRotation(offsetXTime, offsetYTime):
    first = offsetXTime
    second = offsetYTime

    if(offsetYTime > offsetXTime):
        first = offsetYTime
        second = offsetXTime

    currentTime = time.time()
    while(True):
        if(temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
        end = time.time()
        if((end - currentTime) > first):
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            break

    time.sleep(3)

    currentTime = time.time()
    while(True):
        if(temp2==1):
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
        end = time.time()
        if((end - currentTime) > second):
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)
            break
    GPIO.cleanup()
    print("Motor rotation successful")
    
def resetPosition():
    currentTime = time.time()
    while(True):
        if(temp2==1):
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
        end = time.time()
        if((end - currentTime) > full_rotation_time):
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            break
    GPIO.cleanup()