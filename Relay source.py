import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

while(True):
        GPIO.output(12,True)
        print("true")
        time.sleep(2)
        
        GPIO.output(12,False)
        print("false")
        time.sleep(2)
        


GPIO.cleanup()