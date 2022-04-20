import camera
import switch
import sensor
import time
import aws_PubSub
import play_audio
import FCM
import streaming
import os
import blescan
import text_to_speech
import voice_record

nobody_count = 0
READY = 150

pic_by_sensor = False

def execute_for_sensor():
    global pictureCount
    global nobody_count
    global READY
    global pic_by_sensor
    
    while True:
        time.sleep(0.2)

        if (sensor.get_motion_flag() or sensor.get_distance_flag()):
            if (pic_by_sensor == False):
                if(blescan.get_detected_flag() == False):
                    aws_PubSub.publish_message("Sensor", "Somebody came")
                    FCM.push_alarm("Somebody came","Visitor")
                camera.take_picture()
                pic_by_sensor = True
                
            nobody_count = 0
        else :
            if (nobody_count == READY):
                
                switch.set_switch_flag(False)
                pic_by_sensor = False
                nobody_count = 0
                pictureCount = 0
                if(voice_record.getStatus() == False):
                    text_to_speech.set_respond(False)
                print ("----- SAFTY SYSTEM : Safty system reset -----\n")
                streaming.streaming_stop()
            else :
                nobody_count += 1
                
def execute_for_bell():
    global nobody_count
    
    while True:
        time.sleep(0.2)
        if (switch.switch_press_check()):
            aws_PubSub.publish_message("Switch", "Bell Pressed")
            FCM.push_alarm("Visitor pressed the bell","Bell")
            nobody_count = 0
            
def execute_for_srien():
    while True:
        time.sleep(0.2)
        if (aws_PubSub.get_message() != None):
            message = aws_PubSub.get_message()
            if (message.topic == "Siren"):
                aws_PubSub.reset_message()
                print ("----- SAFTY SYSTEM : Siren ringing -----\n")
                play_audio.play_audio("siren")

        
def execute_for_reboot():
    while True:
        time.sleep(0.2)
        if (aws_PubSub.get_message() != None):
            message = aws_PubSub.get_message()
            if (message.topic == "Reboot"):
                aws_PubSub.reset_message()
                print ("----- SAFTY SYSTEM : Rebooting... -----\n")
                os.system("sudo reboot -f")

    

        
