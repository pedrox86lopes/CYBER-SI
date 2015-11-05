# Author: Jamie Shaw
# Description: Parses an Nmap XML file to pull out the SSL certificate issuer. This relies on the ssl-cert nse script being used.
# Usage: ./Python-SSLissuer.py <nmapscan.xml>

from lxml import etree
import sys

nmapFile = sys.argv[1]

xml = etree.parse(open(nmapFile))

for host in xml.xpath("//host"):
	for addr in host.xpath("address/@addr"):
		print "------------------------------"
		print "Host: " + addr
	for port in host.xpath("ports/port"):
		for issuer in port.xpath('script[@id="ssl-cert"]/table[@key="issuer"]/elem[@key="commonName"]'):
			print "Issuer: " + issuer.text