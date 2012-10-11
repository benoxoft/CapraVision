import socket
import time

def test():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(("127.0.0.1", 5030))
	s.send("CREATE TYPE=filterchain ID=my_filterchain\n")
	time.sleep(1)
	s.send("CREATE TYPE=filter TYPE=GRAYSCALE2RGB ID=my_g2r")
	time.sleep(1)
	s.send("SAVE OID=my_filterchain ID")
	s.close()

