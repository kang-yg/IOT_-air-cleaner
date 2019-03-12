import RPi.GPIO as GPIO
import time

soilMoistureSensor = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(soilMoistureSensor,GPIO.IN)

def callback(soilMoistureSensor):
    if GPIO.input(soilMoistureSensor):
        print("No water detected")
    else:
        print("Water detected")
        
GPIO.add_event_detect(soilMoistureSensor, GPIO.BOTH, bouncetime = 300)
GPIO.add_event_callback(soilMoistureSensor, callback)

while True:
    time.sleep(1)