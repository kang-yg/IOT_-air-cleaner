from socket import socket

client_socket = socket()
# 기본적인 클라이언트 소켓을 만든다

ip = '127.0.0.1'
# 원하는 ip와 port를 설정하고
port = 9999

client_socket.connect((ip, port))
# 해당 소켓을 연결한다!! 코틀린과의 다른점
while 1:
	data = '여기에 데이터를 입력하세요.'
	# data를 encode한 후 send에 넣습니다.
	client_socket.send(data.encode('utf-8'))

	data = client_socket.recv(1024).decode('utf-8')
	# 1024라는 사이즈를 설정하여 받은 데이터를 utf-8로 decode합니다.
	print(data)
