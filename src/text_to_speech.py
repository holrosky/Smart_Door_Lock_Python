import aws_PubSub
import time
import play_audio
from gtts import gTTS

responded_to_visitor = False

def get_respond():
    global responded_to_visitor
    return responded_to_visitor

def set_respond(flg):
    global responded_to_visitor
    responded_to_visitor = flg

def execute():
    global responded_to_visitor
    while True:
        time.sleep(0.1)
        if (aws_PubSub.get_message() != None):
            message = aws_PubSub.get_message()
            if (message.topic == "TTS"):
                responded_to_visitor = True
                aws_PubSub.reset_message()
                print ("----- TTS : TTS receieved -----\n")
                tts = gTTS(text=str(message.payload), lang='en')
                tts.save("/home/pi/Smart_Door_Lock/sound/TTS.mp3")
                play_audio.play_audio("TTS")
