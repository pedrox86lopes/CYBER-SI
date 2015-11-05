#simple packet sniffer
#U Need sudo or root :_)

import	socket

sniffa = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#PEGA PACOTES 
while True:
	print sniffa.recvfrom(65565)
