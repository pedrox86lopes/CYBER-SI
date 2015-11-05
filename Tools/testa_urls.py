import urllib

pages = ["/area31.html", "/dilma.html", "/coffnix_viado.html", "/coffnix_da_a_bunda.html"]

for page in pages:
    url = urllib.urlopen("http://192.168.0.100"+page)
    print "[+] " + url.url + " [" + str(url.getcode()) + "] "
