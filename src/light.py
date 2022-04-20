import RPi.GPIO as GPIO
import sensor
import time

LIGHT = 23

def execute():
    while True:
        time.sleep(0.5)
        if (sensor.get_motion_flag()):
            print ("----- LIGHT : Light on -----\n")
            GPIO.output(LIGHT, GPIO.LOW)
            time.sleep(30)
            
        else:
            GPIO.output(LIGHT, GPIO.HIGH)
            time.sleep(0.2)
        
