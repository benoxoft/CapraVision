import socket
import time

def test():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1", 5030))
	s.send("NewFilterchainCommand")
	time.sleep(1)
	s.send("AddFilterCommand")
	time.sleep(1)
	s.send("SaveFilterchainCommand")
	s.close()

