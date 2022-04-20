import pyaudio
import wave
import file_manage
import switch
import play_audio
import text_to_speech
import aws_S3
import time
import streaming
import RPi.GPIO as GPIO

MIC_LED = 6
isRunning = False

def record():
    global isRunning
    
    file_manage.make_dir("voice_message")
    file_name = "[voic_message]" + file_manage.get_time() + ".wav"
    wav_output_filename = file_manage.get_path() + file_name
    
    form_1 = pyaudio.paInt16 # 16-bit resolution
    chans = 1 # 1 channel
    samp_rate = 44100 # 44.1kHz sampling rate
    chunk = 4096 # 2^12 samples for buffer
    record_secs = 10 # seconds to record
    dev_index = 0 # device index found by p.get_device_info_by_index(ii)

    audio = pyaudio.PyAudio() # create pyaudio instantiation
    
    #print get_device_info_by_index(5)
    
    for i in range(audio.get_device_count()):
        print audio.get_device_info_by_index(i).get("name")
        if "AK" in audio.get_device_info_by_index(i).get("name"):
            dev_index = i
    
    
    # create pyaudio stream
    stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                        input_device_index = dev_index,input = True, \
                        frames_per_buffer=chunk)
    
    GPIO.output(MIC_LED, 1)
    print("----- VOICE RECORD : Recording... -----\n")
    frames = []

    # loop through stream and append audio chunks to frame array
    for ii in range(0,int((samp_rate/chunk)*record_secs)):
        data = stream.read(chunk)
        frames.append(data)

    print("----- VOICE RECORD : Finished recording -----\n")
    GPIO.output(MIC_LED, 0)
    play_audio.play_audio("record_finish")

    # stop the stream, close it, and terminate the pyaudio instantiation
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # save the audio frames as .wav file
    wavefile = wave.open(wav_output_filename,'wb')
    wavefile.setnchannels(chans)
    wavefile.setsampwidth(audio.get_sample_size(form_1))
    wavefile.setframerate(samp_rate)
    wavefile.writeframes(b''.join(frames))
    wavefile.close()
    isRunning = False
    aws_S3.upload(wav_output_filename, file_manage.get_today() + "/" + file_name, 'voicemsgbucket')

def execute():
    global isRunning
    
    while True:
        time.sleep(0.2)
        if (switch.switch_press_check()):
            isRunning = True
            time.sleep(30)
            if (text_to_speech.get_respond() == False):
                streaming.streaming_stop()
                play_audio.play_audio("record")
                time.sleep(5)
                record()
            isRunning = False
            
def getStatus():
    global isRunning
    return isRunning

    