#!/usr/bin/python

# PortPuller
# Quick and dirty script to pull open ports from nmap scans to feed into Nessus scan.
# Author: cy7h3 (@jlshaw87)
# Date: 31/10/2015
# Version 0.1

import os
import sys

os.system("clear")

if len(sys.argv) < 2:
	print "Please provide an nmap file!"
	sys.exit(0)

nmapfile = sys.argv[1]

command = " grep 'open' "+ nmapfile +" | cut -d'/' -f1 | grep -v 'Nmap' | sort -u | tr '\\n' ','"
process = os.popen(command)

print "Ports pulled from the scan:"
print "-" * 27
print

print str(process.read())
print