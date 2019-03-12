import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pin_name = 11

def rc_time(pin_name):
    count = 0
    
    GPIO.setup(pin_name, GPIO.OUT)
    GPIO.output(pin_name, GPIO.LOW)
    
    time.sleep(0.1)
    
    GPIO.setup(pin_name, GPIO.IN)
    
    while(GPIO.input(pin_name) == GPIO.LOW):
        count += 1
        return count
    
try:
    while True:
        print (rc_time(pin_name))
        
except keyboardInterrupt:
    pass
finally:
    GPIO.cleanup()