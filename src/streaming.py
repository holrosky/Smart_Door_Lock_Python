import os
import safty_system
import sensor
import time
import camera
import subprocess
import blescan
import voice_record
import RPi.GPIO as GPIO

CAMERA_LED = 5
MIC_LED = 6
is_running = False
        
def execute():
    global is_running
    
    while True:
        time.sleep(0.2)
        if ((sensor.get_motion_flag() or sensor.get_distance_flag())and is_running == False and voice_record.getStatus() == False):
            if(blescan.get_detected_flag() == False):
                time.sleep(2)
                while(camera.get_camera_flag() == True):
                    time.sleep(0.2)
                time.sleep(0.5)
                is_running = True
                GPIO.output(CAMERA_LED, 1)
                GPIO.output(MIC_LED, 1)
                print ("----- STREAMING : Streaming starting... -----\n")
                os.system("raspivid --nopreview -md 4 -w 640 -h 480 -fps 15 -t 0 -b 200000 -g 30 -n -o - | ffmpeg -y -xerror -thread_queue_size 32K -f h264 -r 15 -itsoffset 0 -i - -f alsa -ar 11025 -itsoffset 5.5 -async 1 -ac 1 -thread_queue_size 32K -i hw:1,0  -c:a aac -b:a 32k -async 1 -c:v copy -f flv -flags:v +global_header -rtmp_buffer 10000 -r 15 -async 1 rtmp://live.justin.tv/app/live_182822961_NJlJBC12xIAgJ6yLXH1Kr01m2FTE41")
            else:
                time.sleep(2)
                while(camera.get_camera_flag() == True):
                    time.sleep(0.2)
                time.sleep(0.5)
                is_running = True
                GPIO.output(CAMERA_LED, 1)
                print ("----- STREAMING : Monitor streaming starting... -----\n")
                os.system("echo 0 | sudo tee /sys/class/backlight/rpi_backlight/bl_power > /dev/null")
                os.system("raspivid -t 0 -fps 25 -w 800 -h 480 -hf -b 2000000 -o -")

##def streaming_start():
##    global is_running
##
##    if (is_running == False and voice_record.getStatus() == False):
##        if(blescan.get_detected_flag() == False):
##            is_running = True
##            GPIO.output(CAMERA_LED, 1)
##            GPIO.output(MIC_LED, 1)
##            print ("----- STREAMING : Streaming starting... -----\n")
##            os.system("raspivid --nopreview -md 4 -w 640 -h 480 -fps 15 -t 0 -b 200000 -g 30 -n -o - | ffmpeg -y -xerror -thread_queue_size 32K -f h264 -r 15 -itsoffset 0 -i - -f alsa -ar 11025 -itsoffset 5.5 -async 1 -ac 1 -thread_queue_size 32K -i hw:1,0  -c:a aac -b:a 32k -async 1 -c:v copy -f flv -flags:v +global_header -rtmp_buffer 10000 -r 15 -async 1 rtmp://live.justin.tv/app/live_182822961_NJlJBC12xIAgJ6yLXH1Kr01m2FTE41")
##        else:
##            is_running = True
##            GPIO.output(CAMERA_LED, 1)
##            print ("----- STREAMING : Monitor streaming starting... -----\n")
##            os.system("echo 0 | sudo tee /sys/class/backlight/rpi_backlight/bl_power > /dev/null")
##            os.system("raspivid -t 0 -fps 25 -w 640 -h 360 -hf -b 2000000 -o -")
            
def streaming_stop():
    global is_running
    GPIO.output(CAMERA_LED, 0)
    GPIO.output(MIC_LED, 0)
    os.system("sudo killall -9 raspivid")
    os.system("sudo killall -9 ffmpeg")
    os.system("echo 1 | sudo tee /sys/class/backlight/rpi_backlight/bl_power > /dev/null")
    is_running = False
    print ("----- STREAMING : Streaming stop... -----\n")


        
    