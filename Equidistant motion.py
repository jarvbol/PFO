import RPi.GPIO as GPIO
import time

#import multiprocessing
 
out1 = 4
out2 = 17
out3 = 22
out4 = 27

out5 = 14
out6 = 15
out7 = 23
out8 = 24

out9 = 26
out10 = 20
out11 = 21
out12 = 16

out13 = 1
out14 = 5
out15 = 0
out16 = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)

servo = GPIO.PWM(13,50)
servo.start(0)

outN20_1 = 7
outN20_2 = 8
outN20_pwm = 12

# careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
motor1_PinState = 0b0001

step_sleep = 0.001
 
step_count = 3000;

wheel_diametr = 9;
 
# setting up
GPIO.setmode( GPIO.BCM )
GPIO.setup( out1, GPIO.OUT )
GPIO.setup( out2, GPIO.OUT )
GPIO.setup( out3, GPIO.OUT )
GPIO.setup( out4, GPIO.OUT )
GPIO.setup( out5, GPIO.OUT )
GPIO.setup( out6, GPIO.OUT )
GPIO.setup( out7, GPIO.OUT )
GPIO.setup( out8, GPIO.OUT )
GPIO.setup( out9, GPIO.OUT)
GPIO.setup( out10, GPIO.OUT)
GPIO.setup( out11, GPIO.OUT)
GPIO.setup( out12, GPIO.OUT)
GPIO.setup( out13, GPIO.OUT)
GPIO.setup( out14, GPIO.OUT)
GPIO.setup( out15, GPIO.OUT)
GPIO.setup( out16, GPIO.OUT)

GPIO.setup( outN20_1, GPIO.OUT)
GPIO.setup( outN20_2, GPIO.OUT)




 
# initializing
GPIO.output( out1, GPIO.LOW )
GPIO.output( out2, GPIO.LOW )
GPIO.output( out3, GPIO.LOW )
GPIO.output( out4, GPIO.LOW )
GPIO.output( out5, GPIO.LOW )
GPIO.output( out6, GPIO.LOW )
GPIO.output( out7, GPIO.LOW )
GPIO.output( out8, GPIO.LOW )
GPIO.output( out9, GPIO.LOW)
GPIO.output( out10, GPIO.LOW)
GPIO.output( out11, GPIO.LOW)
GPIO.output( out12, GPIO.LOW)
GPIO.output( out13, GPIO.LOW)
GPIO.output( out14, GPIO.LOW)
GPIO.output( out15, GPIO.LOW)
GPIO.output( out16, GPIO.LOW)

GPIO.output(outN20_1, GPIO.LOW)
GPIO.output(outN20_2, GPIO.LOW)


def moving_forward(steps_total, steps_accel, time_at_start, time_on_march ,pin1, pin2,pin3, pin4): # Тестовая функция для отладки моторов на движение.
 
    i = 0

    time_current = time_at_start
    time_delta = (time_at_start - time_on_march)/steps_accel # делим разность между длительностью импульса в начале разгона и конце разгона на число шагов для разгона

    for i in range(steps_total):
        GPIO.output(pin4, motor1_PinState & 0b0001)
        GPIO.output(pin3, motor1_PinState & 0b0010)
        GPIO.output(pin2, motor1_PinState & 0b0100)
        GPIO.output(pin1, motor1_PinState & 0b1000)

        time.sleep(time_current)
        if i<steps_accel:
            time_current = time_current - time_delta # с каждым шагом сокращаем длительность импульса. Насколько плавно получится - вопрос.

        motor1_PinState << 1
        if motor1_PinState > 4:
            motor1_PinState = 1