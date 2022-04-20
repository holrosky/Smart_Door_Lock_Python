import RPi.GPIO as GPIO
import aws_PubSub
import play_audio
import blescan
import time

DOOR = 24
DOOR_STATUS = 4

def execute():
    while True:
        time.sleep(0.2)
        if (aws_PubSub.get_message() != None):
            message = aws_PubSub.get_message()
            if (message.topic == "Door"):
                if(message.payload == "Door button"):
                    door_open()
                elif(message.payload == "Shake"):
                    if(blescan.get_detected_flag() == True):
                        door_open()
                    else:
                        print ("----- FAIL TO OPEN : Phone is not near by -----\n")
                        aws_PubSub.reset_message()
                        
def door_status():
    while True:
        time.sleep(1)
        if (GPIO.input(DOOR_STATUS)):
            aws_PubSub.publish_message("Door status", "open")
        else:
            aws_PubSub.publish_message("Door status", "close")

def door_open():
    aws_PubSub.reset_message()
    print ("----- DOOR : Door is open -----\n")
    GPIO.output(DOOR, GPIO.LOW)
    play_audio.play_audio("door")
    GPIO.output(DOOR, GPIO.HIGH)
                    
