import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
P = GPIO.PWM(11,50)
try:
    while True:
        P.start(0)
        P.ChangeDutyCycle(3)
        sleep(1)
        P.ChangeDutyCycle(12)
        sleep(1)
except KeyboardInterrupt:
    P.stop()
    GPIO.cleanup()# Echo server program
import socket

HOST = '127.0.0.1'                   # Symbolic name meaning all available interfaces
PORT = 9999              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by'), addr
while 1:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
