import sys
import socket

#I Need to resolv that option here, help, hey jude, helpme

from optparse import OptionParser
parser = OptionParser()
parser.add_option("-f", "--file", dest="filename",help="write report to FILE", metavar="FILE")

#codes here

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("whois.arin.net", 43))

s.send((sys.argv[1] + "\r\n").encode())

response = b""
while True:
    data = s.recv(4096)
    response += data
    if not data:
       break
s.close()

print(response.decode())
