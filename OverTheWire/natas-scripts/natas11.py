import base64
import json

c = b"HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GIjEJAyIxTRg="
c = base64.decodebytes(c)

p = {"showpassword":"no", "bgcolor":"#ffffff"}

p = json.dumps(p).encode('utf-8').replace(b" ",b"")

def xor(p,c):
	secret = ""
	for x in range(len(p)):
		secret += str(chr(c[x] ^ p[x % len(p)]))
	return secret

secret = xor(c,p)
print(secret) 

# Create now the new cookie setting showpassword to yes

key = b"eDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoeDWoe"  #secret
new_cookie = {"showpassword":"yes", "bgcolor":"#ffffff"}
new_cookie = json.dumps(new_cookie).encode('utf-8').replace(b" ",b"")

data = xor(key, new_cookie)
data = base64.encodebytes(data.encode('utf-8'))

print(f"Cookie: {data}")



