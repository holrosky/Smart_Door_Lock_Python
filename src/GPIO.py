import RPi.GPIO as GPIO


def set_up():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    MOTION = 17
    MOTION_LED = 27
    DISTANCE_ECHO = 20
    DISTANCE_TRRIGER = 21
    DISTANCE_LED = 16
    SWITCH = 18
    CAMERA_LED = 5
    MIC_LED = 6
    LIGHT = 23
    DOOR = 24
    DOOR_STATUS = 4

    GPIO.setup(SWITCH,GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(DOOR_STATUS, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(MOTION, GPIO.IN)
    GPIO.setup(MOTION_LED, GPIO.OUT)
    GPIO.setup(DISTANCE_ECHO, GPIO.IN)
    GPIO.setup(DISTANCE_TRRIGER, GPIO.OUT)
    GPIO.setup(DISTANCE_LED, GPIO.OUT)
    GPIO.setup(CAMERA_LED, GPIO.OUT)
    GPIO.setup(MIC_LED, GPIO.OUT)
    GPIO.setup(LIGHT, GPIO.OUT)
    GPIO.setup(DOOR, GPIO.OUT)
    
    GPIO.output(LIGHT, GPIO.HIGH)
    GPIO.output(DOOR, GPIO.HIGH)
    GPIO.output(DISTANCE_TRRIGER, GPIO.LOW)