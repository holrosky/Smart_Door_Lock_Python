'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time
import json

AllowedActions = ['both', 'publish', 'subscribe']
global_message = None
lock = False
# Custom MQTT message callback
def customCallback(client, userdata, message):
    global global_message
##    print ("--------- Subscribe ---------")
##    print "topic: " + message.topic
##    print "message: " + message.payload
##    print ("-----------------------------\n")
    global_message = message

def publish_message(topic, message):
##    print ("--------- Publish ---------")
##    print "topic: " + topic
##    print "message: " + str(message)
##    print ("---------------------------\n")
    messageJson = json.dumps(message)
    try:
        myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    except:
        print ("Error occured. Connection lost")
        while True:
            time.sleep(1)
            try:
                myAWSIoTMQTTClient.connect()
                break
            except:
                print ("Reconnecting...")
        myAWSIoTMQTTClient.publish(topic, messageJson, 1)
    
def get_message():
    global global_message
    return global_message

def reset_message():
    global global_message
    global_message = None

host = "a29ljsynycxctz-ats.iot.eu-west-2.amazonaws.com"
rootCAPath = "/home/pi/Smart_Door_Lock/CA/root-CA.crt"
certificatePath = "/home/pi/Smart_Door_Lock/CA/Smart_Door_Lock.cert.pem"
privateKeyPath = "/home/pi/Smart_Door_Lock/CA/Smart_Door_Lock.private.key"
port = 8883
clientId = "Smart_Door_Lock"

# Configure logging
#logger = logging.getLogger("AWSIoTPythonSDK.core")
#logger.setLevel(logging.DEBUG)
#streamHandler = logging.StreamHandler()
#formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#streamHandler.setFormatter(formatter)
#logger.addHandler(streamHandler)

# Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None

myAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
myAWSIoTMQTTClient.configureEndpoint(host, port)
myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()

publish_message("Connection", "Raspberry Pi Connected")
myAWSIoTMQTTClient.subscribe("#", 1, customCallback)
time.sleep(0.5)