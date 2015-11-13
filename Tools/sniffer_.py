#simple packet sniffer
#U Need sudo or root :_)

import	socket

sniffa = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

#PEGA PACOTES 
while True:
	print sniffa.recvfrom(65565)

for sniffado in sniffa.stdout:
    if "!BBHHHBBH4s4s" in sniffa:
        print ("[+]"+str(sniffado.rstrip()[21:]))

    if IP[0:12] in sniffado:
        print ("YOU==>"+str(sniffa.rstrip()))



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print 'Sniffer parado!'
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

