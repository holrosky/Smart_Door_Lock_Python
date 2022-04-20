from pyfcm import FCMNotification
import time
import aws_PubSub
 
push_service = FCMNotification(api_key="AAAACIh1870:APA91bEr8Q8BZ94O_JDWzXw4re6UqtL1tky_3kEIlUSgOl3-SBhJ9eBsx_dSUHvXK0ShT3gYWTcra6D5nc9QqT8lB6OoFzGYQKRUdhrYfXv5vCvckLPtHPdFYzydaMSjvWtrzEQzPMiE")
 
#registration_id = "cXkl8BmiFAc:APA91bE9G5j4njQ0wvc3SJ0Yv1dSkti4vV-Vy58A2vNtnGSA_-3v3RS1EwYagduqeQtKwstmzc92AVqdfXgZ2zld5UpvKl5v4krTf_LY29fDsYMT6_a6iaiVxSL5cIm_lCVV4psgZAk0"
#registration_id = "e2LFUp9r_dE:APA91bHwhyXAf1nmOq1eHFJy9mJMi8ylsvQKU-YqauD8F--O4z7hwO54V6-VKB9xdiZBYotNRa6gTlWeA19BR81mgzCUAMgfk9QH6PzX_5XE3kpL5SjXFyWssFYTXNNJUchTYkwliue0"

registration_ids = []

with open('/home/pi/Smart_Door_Lock/token.txt','rb') as token:
  lines = token.read().split()
  for line in lines:
    registration_ids.append(line)

def push_alarm(message, title):
    if registration_ids :
        message_title = title
        message_body = message
        result = push_service.notify_multiple_devices(registration_ids=registration_ids, message_body=message, message_title=title, sound="default")

def registration():
    #global registration_ids
    
    while True:
        time.sleep(0.1)
        if (aws_PubSub.get_message() != None):
            message = aws_PubSub.get_message()
            if (message.topic == "Registraion"):
                if not message.payload in registration_ids:
                    registration_ids.append(message.payload)
                    file = open('/home/pi/Smart_Door_Lock/token.txt', 'ab')
                    file.write(message.payload + "\n")
                    file.close()
        
    