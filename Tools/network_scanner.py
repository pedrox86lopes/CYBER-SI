import commands
import subprocess as sub

IP = commands.getoutput("hostname -i")

proccess= sub.Popen(("nmap","-sP","191.168.0.1/24"),stdout= sub.PIPE) 

for fila in proccess.stdout:
    if "Nmap scan report for" in fila:
        print ("[+]"+str(fila.rstrip()[21:]))

    if IP[0:12] in fila:
        print ("YOU==>"+str(fila.rstrip()))


