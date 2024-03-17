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



def stop(): #Остановка движения мотора N20.
    GPIO.output(outN20_1, GPIO.LOW) 
    GPIO.output(outN20_2, GPIO.LOW)
    
    
def forward(t): #Движение  мотора N20 вниз.
    GPIO.output(outN20_1, GPIO.HIGH)
    time.sleep(t)
    stop();
    cleanup();
    return 0;

def backward(t): #Движение  мотора N20 вверх.
    GPIO.output(outN20_2, GPIO.HIGH)
    time.sleep(t)
    stop()
    return 0;



def distance(distance):
    step = int(((distance/(3.14 * wheel_diametr))*360)/200);
    return step;
 
def cleanup(): # Обнуление пинов, чтобы избежать посторонних шумов.
    GPIO.output( out1, GPIO.LOW )
    GPIO.output( out2, GPIO.LOW )
    GPIO.output( out3, GPIO.LOW )
    GPIO.output( out4, GPIO.LOW )
    GPIO.output( out5, GPIO.LOW )
    GPIO.output( out6, GPIO.LOW )
    GPIO.output( out7, GPIO.LOW )
    GPIO.output( out8, GPIO.LOW )
    GPIO.output( out9, GPIO.LOW)
    GPIO.output( out10,GPIO.LOW)
    GPIO.output( out11, GPIO.LOW)
    GPIO.output( out12, GPIO.LOW)
    GPIO.output( out13, GPIO.LOW)
    GPIO.output( out14,GPIO.LOW)
    GPIO.output( out15, GPIO.LOW)
    GPIO.output( out16, GPIO.LOW)
    GPIO.cleanup()
 
def moving_forward(step,pin1, pin2,pin3, pin4): # Тестовая функция для отладки моторов на движение.

    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
 
        time.sleep( 0.008 )
        
def rail(step, flag): # Функция обеспечивающая движение рейки вперед и назад. Если flag = 1, рейка движется вперед, если flag = 0, рейка движется назад.
    if flag == 1: 
        pin1,pin2,pin3,pin4 = out13,out14,out15,out16;
    if flag == 0:
        pin1,pin2,pin3,pin4 = out16,out15,out14,out13;
    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
 
        time.sleep( 0.003 )
    
def lifting_the_rail(step, flag): # Функция обеспечивающая подъем и опускание рейки. Если flag = 1, рейка поднимается, если flag = 0, рейка опускается.
    if flag == 1: 
        pin1,pin2,pin3,pin4 = out9,out10,out11,out12;
    if flag == 0:
        pin1,pin2,pin3,pin4 = out12,out11,out10,out9;
    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
 
        time.sleep( 0.01)
    GPIO.output( out9, GPIO.HIGH )
    GPIO.output( out10, GPIO.HIGH )
    GPIO.output( out11, GPIO.HIGH )
    GPIO.output( out12, GPIO.HIGH )   
    time.sleep(5);
    
def lift_der(): # Попытка написания функции для удержания мотора в напряжении, дабы рейка произвольно не опускалась.
        GPIO.output( out9, GPIO.HIGH )
        GPIO.output( out10, GPIO.HIGH )
        GPIO.output( out11, GPIO.HIGH )
        GPIO.output( out12, GPIO.HIGH )
    
def moving_backwards(step,pin1, pin2,pin3, pin4): # Отладочная функция движения мотора назад.
    

    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
 
        time.sleep( step_sleep )
        
def moving_backwards_two_motors(step,pin1, pin2,pin3, pin4,pin5, pin6,pin7, pin8): # Отладочная функция движения обоих моторов назад.
    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.HIGH )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.HIGH )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.HIGH )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.HIGH )
 
        time.sleep( step_sleep )
    
def moving_forward_two_motors(step,pin1, pin2,pin3, pin4,pin5, pin6,pin7, pin8): # Отладочная функция движения вперед двумя моторами.
    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.HIGH )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.HIGH )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.HIGH )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.HIGH )
 
        time.sleep( step_sleep )

def moving_two_motor(step,flag): # Функция для управления моторами на движение в двух направлениях. Если flag = 1, робот движется вперед, когда flag = 0, робот движется назад.
    if flag == 1: 
        pin1,pin2,pin3,pin4, pin5,pin6, pin7, pin8 = out4,out3,out2,out1,out5,out6,out7,out8;
    if flag == 0:
        pin1,pin2,pin3,pin4, pin5,pin6, pin7, pin8 = out1,out2,out3,out4,out8,out7,out6,out5;
    i = 0
    for i in range(step):
        if i%4==0:
            GPIO.output( pin4, GPIO.HIGH )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.HIGH )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==1:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.HIGH )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.HIGH )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==2:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.HIGH )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.LOW )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.HIGH )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.LOW )
        elif i%4==3:
            GPIO.output( pin4, GPIO.LOW )
            GPIO.output( pin3, GPIO.LOW )
            GPIO.output( pin2, GPIO.LOW )
            GPIO.output( pin1, GPIO.HIGH )
            GPIO.output( pin8, GPIO.LOW )
            GPIO.output( pin7, GPIO.LOW )
            GPIO.output( pin6, GPIO.LOW )
            GPIO.output( pin5, GPIO.HIGH )
 
        time.sleep( 0.005 )

#moving_backwards_two_motors(step_count, out1,out2,out3,out4,out5,out6,out7,out8);
#moving_forward_two_motors(step_count, out4,out3,out2,out1,out5,out6,out7,out8);

#time.sleep(2);
#moving_two_motor(step_count,1)
#moving_backwards(30000, out9,out10,out11,out12);  
#time.sleep(2);
#moving_fo
# rward(step_count, out5,out6,out7,out8);
#sosalka_work()
#moving_forward(200, out13, out14, out15, out16)
#moving_backwards(step_count, out8, out7, out6, out5)


#rail(600, 0);


#forward(0.1)
#time.sleep(2)

#time.sleep(20);
#backward(0.1)
#moving_forward(100,out5, out6, out7, out8)
#moving_two_motor(500,1)
lifting_the_rail(90,1);

#rail(1500,0)
#forward(0.1)


cleanup();
exit( 0 );
