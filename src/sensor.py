import RPi.GPIO as GPIO
import time

motion_flag = False
MOTION = 17
MOTION_LED = 27

distance_flag = False
DISTANCE_ECHO = 20
DISTANCE_TRRIGER = 21
DISTANCE_LED = 16

def motion_execute():
    global motion_flag
    
    while True:
        time.sleep(3)
        
        if (GPIO.input(MOTION)):
            print("----- SENSOR : Motion detected -----\n")
            motion_flag = True
            GPIO.output(MOTION_LED, 1)
                
        else:
            time.sleep(0.1)
            motion_flag = False
            GPIO.output(MOTION_LED, 0)
            
def distance_execute():
    global distance_flag
    
    while True:
        time.sleep(1)
        GPIO.output(DISTANCE_TRRIGER, GPIO.HIGH)

        time.sleep(0.0001)

        GPIO.output(DISTANCE_TRRIGER, GPIO.LOW)

        while GPIO.input(DISTANCE_ECHO)==0:
            pulse_start_time = time.time()
        while GPIO.input(DISTANCE_ECHO)==1:
            pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round(pulse_duration * 17150, 2)
        
        if(distance < 40):
            distance_flag = True
            print("----- SENSOR : Distance detected -----\n")
            GPIO.output(DISTANCE_LED, 1)
        else:
            distance_flag = False
            GPIO.output(DISTANCE_LED, 0)

def get_distance_flag():
    global motion_flag
    return motion_flag

def get_motion_flag():
    global distance_flag
    return distance_flag