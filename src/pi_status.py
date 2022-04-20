import aws_PubSub
import time

def execute():
    while True:
        aws_PubSub.publish_message("Raspberry pi status", "ON")
        time.sleep(1)
    