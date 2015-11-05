import urllib2
import sys

url = sys.argv[1]

req = urllib2.Request(url)
res = urllib2.urlopen(req)

RetHeaders = res.headers

print "URL: " + url + "\n"

print "---- Security Headers Found ----\n"

if "Strict-Transport-Security" in RetHeaders:
    print "[-] Security Header Found: Strict-Transport-Security"

if "X-Frame-Options" in RetHeaders:
    print "[-] Security Header Found: X-Frame-Options"

if "X-XSS-Protection" in RetHeaders:
    print "[-] Security Header Found: X-XSS-Protection"

if "X-Content-Type-Options" in RetHeaders:
    print "[-] Security Header Found: X-Content-Type-Options"

if "Content-Security-Policy" in RetHeaders:
    print "[-] Security Header Found: Content-Security-Policy"

print "\n---- Missing Headers ----\n"

if "Strict-Transport-Security" not in RetHeaders:
    print "[-] Missing Header: Strict-Transport-Security"

if "X-Frame-Options" not in RetHeaders:
    print "[-] Missing Header: X-Frame-Options"

if "X-XSS-Protection" not in RetHeaders:
    print "[-] Missing Header: X-XSS-Protection"

if "X-Content-Type-Options" not in RetHeaders:
    print "[-] Missing Header: X-Content-Type-Options"

if "Content-Security-Policy" not in RetHeaders:
    print "[-] Missing Header: Content-Security-Policy"

res.close()