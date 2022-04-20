import base64
import aws_PubSub

def publish(file):
    with open(file, "rb") as imageFile:
        encoded_file = base64.b64encode(imageFile.read())
        aws_PubSub.publish_message("Image", encoded_file)
    

    
