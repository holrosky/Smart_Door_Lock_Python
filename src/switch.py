import RPi.GPIO as GPIO
import time
import camera
import play_audio

switch_flag = False
SWITCH = 18

def switch_press_check():
    input_state = GPIO.input(SWITCH)
    if input_state == False:
        return True
    
def get_switch_flag():
    global switch_flag
    return switch_flag

def set_switch_flag(flag):
    global switch_flag
    switch_flag = flag

def execute():
    global switch_flag
    while True:
        time.sleep(0.2)
        if (switch_press_check()):
            set_switch_flag(True)
            print ("----- Bell : Bell pressed -----\n")
            play_audio.play_audio("bell")
            time.sleep(3)
            play_audio.play_audio("greeting")
