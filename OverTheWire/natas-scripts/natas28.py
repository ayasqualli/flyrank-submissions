#!/usr/bin/python

import requests
import binascii
import urllib
import string
import base64

url = 'http://natas28.natas.labs.overthewire.org'

charset = string.punctuation


s = requests.Session()

s.auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

sample = "aaaaaaaaaaa"


for x in charset:
	data = {'query': sample+x}
	r = s.post(url, data=data)
	cipher = r.url.split('=')[1]
	cipher = urllib.parse.unquote(cipher)
	print ("[*] last char. = %s | %s" %(x, cipher))
