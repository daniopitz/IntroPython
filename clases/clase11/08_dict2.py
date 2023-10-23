ipaddress = {'udd.cl':'201.221.123.142',
             'google.com':'64.233.190.101'}

ip2=ipaddress.copy()

print(ipaddress)

ipaddress['ingenieria.udd.cl'] = '201.221.123.142'
ipaddress['www.pokemongo.com'] = '13.33.131.6'

print('Dirección IP de udd.cl:', ipaddress['udd.cl'])

print('Dirección IP de ingenieria.udd.cl:', ipaddress['ingenieria.udd.cl'])

print(ipaddress)

print(ip2)
