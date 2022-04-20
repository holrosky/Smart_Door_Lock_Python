import os
import file_manage
import aws_S3
import RPi.GPIO as GPIO
import time

CAMERA_LED = 5
is_running = False

def take_picture():
    global is_running
    
    GPIO.output(CAMERA_LED, 1)
    
    is_running = True
    file_name = "[Visitor]" +file_manage.get_time() +".png"
    file_manage.make_dir("picture")
    
    os.system("raspistill -n -w 1920 -h 1080 -o " + file_manage.get_path() + file_name)
    
    GPIO.output(CAMERA_LED, 0)
    print ("-----CAMERA : Picture Taken-----\n")
    
    is_running = False
    time.sleep(2)
    
    aws_S3.upload(file_manage.get_path() + file_name, file_manage.get_today() + "/" + file_name, 'visitorpicturebucket')

def get_camera_flag():
    global is_running
    return is_running
    