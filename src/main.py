import sensor
import GPIO
import switch
import text_to_speech
import safty_system
import light
import door
import FCM
import streaming
import blescan
import pi_status
import voice_record
from threading import Thread

print ("-------------------------------------")
print ("|                                   |")
print ("|    Welcome to Smart Door Lock     |")
print ("|                                   |")
print ("-------------------------------------")

GPIO.set_up()

motion_sensor_thread = Thread(target=sensor.motion_execute)
distance_sensor_thread = Thread(target=sensor.distance_execute)
switch_thread = Thread(target=switch.execute)
safty_sensor_thread = Thread(target=safty_system.execute_for_sensor)
safty_bell_thread = Thread(target=safty_system.execute_for_bell)
safty_siren_thread = Thread(target=safty_system.execute_for_srien)
safty_reboot_thread = Thread(target=safty_system.execute_for_reboot)
text_to_speech_thread = Thread(target=text_to_speech.execute)
light_thread = Thread(target=light.execute)
door_thread = Thread(target=door.execute)
door_status_thread = Thread(target=door.door_status)
FCM_thread = Thread(target=FCM.registration)
streaming_start_thread = Thread(target=streaming.execute)
ble_thread = Thread(target=blescan.execute)
pi_status_thread = Thread(target=pi_status.execute)
voice_record_thread = Thread(target=voice_record.execute)

pi_status_thread.start()
ble_thread.start()
FCM_thread.start()
motion_sensor_thread.start()
distance_sensor_thread.start()
switch_thread.start()
safty_sensor_thread.start()
safty_bell_thread.start()
safty_siren_thread.start()
safty_reboot_thread.start()
text_to_speech_thread.start()
light_thread.start()
door_thread.start()
door_status_thread.start()
streaming_start_thread.start()
voice_record_thread.start()

