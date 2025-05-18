from random import randint
from lfs import *

for x in range(10**9):
	if not (x + 1) & ((1 << 15) - 1):
		print('.', end="", flush=True)
	secret = f"lfsr_are_not_secure{x:08d}"
	flag = create_flag(secret)
	hash = digest(flag.encode())
	enc_hash = base64_encode(hash)
	if enc_hash.startswith("SUS/"):
		print()
		print("secret :", secret)
		break
else:
	assert False

message = "KSUS{".encode()
x = randint(1, 1 << 64)
x <<= 15
while True:
	x += 1
	if not x & ((1 << 15) - 1):
		print('.', end="", flush=True)
	passphrase = str(x)
	key = create_key(passphrase)
	e = scramble(message, key)
	enc_e = base64_encode(e).lower()
	if enc_e.startswith("very/") or enc_e.startswith("very+"):
		print()
		print("passphrase :", passphrase)
		break

challenge = encrypt(flag, passphrase)
print("challenge :", challenge)

