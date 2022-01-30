import RPi.GPIO as GPIO   

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
print("\n")
print("The default speed & direction of the motors is LOW & Forward.\n")
print("To control first motor: ")
print("r1-run s1-stop f1-forward b1-backward l1-low m1-medium h1-high e-exit\n")
print("To control second motor: ")
print("r2-run s2-stop f2-forward b2-backward l2-low m2-medium h2-high e-exit\n")

while(1):

    x = input()
    
    if x=='r1':
        print("run first")
        if(temp1==1):
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            print("forward first")
            x='z'
        else:
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            print("backward first")
            x='z'
            
    elif x=='r2':
        print("run second")
        if(temp2==1):
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            print("forward second")
            x='z'
        else:
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print("backward second")
            x='z'

    elif x=='s1':
        print("stop first")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        x='z'

    elif x=='s2':
        print("stop second")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f1':
        print("forward first")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        temp1=1
        x='z'
        
    elif x=='f2':
        print("forward second")
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp2=1
        x='z'

    elif x=='b1':
        print("backward first")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        temp1=0
        x='z'

    elif x=='b2':
        print("backward second")
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp2=0
        x='z'

    elif x=='l1':
        print("low first")
        p1.ChangeDutyCycle(50)
        x='z'

    elif x=='l2':
        print("low second")
        p2.ChangeDutyCycle(50)
        x='z'

    elif x=='m1':
        print("medium first")
        p1.ChangeDutyCycle(75)
        x='z'

    elif x=='m2':
        print("medium first")
        p2.ChangeDutyCycle(75)
        x='z'

    elif x=='h1':
        print("high first")
        p1.ChangeDutyCycle(100)
        x='z'
     
    elif x=='h2':
        print("high second")
        p2.ChangeDutyCycle(100)
        x='z'
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("Please enter the defined data to continue...")