import vlc
import socket
import RPi.GPIO as GPIO # GPIO library we need to use the GPIO pins
import time # time library for sleep function
import threading

senserSet = ['false','false','false','false']
''' 0:LED, 1:WATER PUMP, 2:FAN 3:SPEAKER '''

#pir 센서 작동
#pir.wait_for_motion() <- pir이 감지되면
#pir.wait_for_no_motion() <-pir이 감지가 안되면

#fanByMan -> human or pir? => 0 : human, 1 : pir

PUMP = 10
FAN = 12
LED = 11
pirNo = 40

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PUMP,GPIO.OUT) #water pump
GPIO.setup(FAN,GPIO.OUT) #FAN
#GPIO.setup(12,GPIO.OUT) #SPEAKER
GPIO.setup(LED,GPIO.OUT) #LED
GPIO.setup(pirNo,GPIO.IN)

fanNo = 10
fanByMan = 0

def pirfunc(pirNo, fanByMan):
    while(1):
        if GPIO.input(pirNo) and senserSer[2] == 'false' :
            print('Motion Detected!!')
            senserSet[2] = 'true'
            '''GPIO.output(FAN핀 넘버,True)'''
            GPIO.output(FAN,True)
            fanByMan = 1
        else if GPIO.input(pirNo)== False :
            if fanByMan == 1:
                if senserSet[2] == 'true' :
                    print('Motion Disappered')
                    senserSet[2] = 'false'
                    GPIO.output(FAN,False)
                    fanByMan = 0
   


HOST = ''                   # Symbolic name meaning all available interfaces
PORT = 9999             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

t = threading.Thread(target=pirfunc,args=(pirNo,fanByMan))
t.daemon = True
t.start()

while 1:
    
    conn, addr = s.accept()
    print ('Connected by')
    print (addr)
    i=0;
    
    statement = '여기에 말을 넣어주세요.';
    senserNo = 0;
    while 1:
        data = conn.recv(1024).decode('utf-8')
        if data:
            if data == 'finished':
                print ('Disconnected')
                conn.close()
                break
            if (conn != None) and (GPIO.input(pirNo)==True) and (fanByMan == 1) :
                statement = 'fanbypir'
                conn.send(statement.encode('utf-8'))
                
            senserNo=data[0];
            number = int(senserNo);
            value = data[1:len(data)];
            if number >= 0 and number < 4:
                if number == 0:
                    if value == 'false':
                        senserSet[number] = 'false'
                        '''GPIO.output(LED핀 넘버,False)'''
                        statement = "LED OFF"
                        GPIO.output(LED,False)
                    else:
                        senserSet[number] = 'true'
                        '''GPIO.output(LED핀 넘버,True)'''
                        statement = "LED ON"
                        GPIO.output(LED,True)
                elif number == 1:
                    if value == 'false':
                        senserSet[number] = 'false'
                        statement = "WATER PUMP OFF"
                        GPIO.output(PUMP,False)
                        time.sleep(2)
                        '''GPIO.output(WATER PUMP핀 넘버,False)'''
                    else:
                        senserSet[number] = 'true'
                        statement = "WATER PUMP ON"
                        GPIO.output(PUMP,True)
                        time.sleep(2)
                        '''GPIO.output(WATER PUMP핀 넘버,True)'''
                elif number == 2:
                    if value == 'false':
                        if fanByMan == 1:
                            fanByMan =0
                        senserSet[number] = 'false'
                        statement = "FAN OFF"
                        GPIO.output(FAN,False)
                        '''GPIO.output(FAN핀 넘버,False)'''
                    else:
                        senserSet[number] = 'true'
                        '''GPIO.output(FAN핀 넘버,True)'''
                        statement = "FAN ON"
                        GPIO.output(FAN,True)
                elif number == 3:
                    if value == 'false':
                        senserSet[number] = 'false'
                        '''GPIO.output(SPEAKER핀 넘버,False)'''
                        statement = "SPEAKER OFF"
#                        GPIO.output(12,False)
                        p.stop()
                    else:
                        senserSet[number] = 'true'
                        '''GPIO.output(SPEAKER핀 넘버,True)'''
                        statement = "SPEAKER ON"
#                        GPIO.output(12,True)
                        p = vlc.MediaPlayer("file:///home/pi/Desktop/Music/조용필 - 여행을 떠나요 (1993).mp3")
                        p.play()
                print(statement)
                conn.send(statement.encode('utf-8'))
            else:
                print("센서값이 잘못되었습니다.")
        else:
            print("데이터가 수신되지 않았습니다.")

    conn.close()



GPIO.cleanup()
