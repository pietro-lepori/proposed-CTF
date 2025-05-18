from lfs import *
from itertools import product

challenge = input("challenge > ")
e, hash = map(base64_decode, challenge.split('#'))
prefix = "KSUS{".encode()

for t in product("0123456789abcdef", repeat=3):
	missing_fragment = "".join(t)
	base_message = prefix + missing_fragment.encode()
	key_stream = [x ^ y for x, y in zip(e, base_message)]
	key = 0
	for x in reversed(key_stream):
		key <<= 8
		key |= x
	message = scramble(e, key)
	if hash == digest(message):
		flag = message.decode()
		break
else:
	assert False

print("key :", key)
print("flag :", flag)

