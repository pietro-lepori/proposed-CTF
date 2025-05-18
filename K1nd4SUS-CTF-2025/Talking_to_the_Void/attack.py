from subprocess import Popen, PIPE
from base64 import b64decode
from time import sleep

cmd = 'python true_server_v2.py'
process = Popen(cmd
, shell=True, text=True
, stdin=PIPE, stdout=PIPE)

def get_line():
	line = process.stdout.readline()
	if not line and process.poll() is not None:
		exit()
	print(line, end='', flush=True)
	return line

def get_lines():
	while True:
		line = get_line()
		if not line:
			sleep(.1)
		if line.startswith("?"):
			break

def send(query):
	print(query)
	query += "\n"
	process.stdin.write(query)
	process.stdin.flush()

def step():
	send("step")
	sleep(.1)
	ans = get_line().strip()
	return ans

def unscramble(secret, message):
	secret = b64decode(secret)
	message = b64decode(message)
	ans = bytes(x ^ y for x, y in zip(secret, message))
	try:
		ans = ans.decode()
	except:
		ans = str(ans)
	return ans

while True:
	get_lines()
	ans = step()
	if ans.startswith("w"):
		break
	get_lines()
	send("reset " + ans)
secret = ans
get_lines()
send("reset")
get_lines()
send("shell 1")
while True:
	line = get_line().rstrip()
	if not line:
		sleep(3)
		continue
	if line.startswith("?"):
		break
	if '.' not in line and ':' not in line:
		print(unscramble(secret, line))
		get_lines()
		break
get_lines()
assert False
