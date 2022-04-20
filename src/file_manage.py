import datetime
import os

path = "/home/pi/Smart_Door_Lock/"
path_with_today = ""

def make_dir(dir_name):
    global path_with_today
    path_with_today = path + dir_name + "/" + get_today()
    
    if not os.path.isdir(path_with_today) :
        os.mkdir(path_with_today)

def get_path():
    global path_with_today
    return path_with_today + "/"
    
    
def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

def get_today():
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    return today