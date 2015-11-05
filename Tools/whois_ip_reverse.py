#pip install dns 
import  socket

from dns import reversename, resolver

rev_name = reversename.from_address('179.183.24.251')
reversed_dnsx = str(resolver.query(rev_name,"PTR")[0])
reversed_dns = socket.gethostbyaddr('179.183.24.251')

reversed_dns[0]
