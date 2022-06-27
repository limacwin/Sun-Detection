import RPi.GPIO as GPIO
import time

in1 = 24
in2 = 23
in3 = 4
in4 = 22
en1 = 25
en2 = 27

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
p1.ChangeDutyCycle(60)
p2.ChangeDutyCycle(15)

time_motor1 = 2
time_motor2 = 4
i = 0

while(i < 1):
    i = i + 1

    #Open Petals
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.HIGH)
    print(f"Motor 1 opening petals: Rotate {time_motor1} secs")
    time.sleep(time_motor1)
    print("Rotation done")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)

    #Do 360 degree Revolve (Clockwise)
    GPIO.output(in3,GPIO.HIGH)
    GPIO.output(in4,GPIO.LOW)
    print(f"Motor 2 revolving structure: Rotate {time_motor2} secs")
    time.sleep(time_motor2)
    print("Rotation done")
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    time.sleep(10)

    #Do 360 degree Revolve (Anti-Clockwise)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.HIGH)
    print(f"Motor 2 revolving structure: Rotate {time_motor2} secs")
    time.sleep(time_motor2)
    print("Rotation done")
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    #Close Petals
    GPIO.output(in1,GPIO.HIGH)
    GPIO.output(in2,GPIO.LOW)
    print(f"Motor 1 closing petals: Rotate {time_motor1} secs")
    time.sleep(time_motor1)
    print("Rotation done")
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    
print("Destructor Called")
#Stopping both Motors
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
print("Motor 1 Stopped")
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
print("Motor 2 Stopped")
GPIO.cleanup()