name:
Talking into the Void

description:
Our sysadmin used to stare into the void, until the void started to stare back at them.
Then they got mad...ly in love!
Now the root user in the server is revealing all our secrets to the void:
```
yes `cat flag.txt` > /dev/null
```
Fortunately, you have access to the system as an unprivileged user.
Unfortunately, you are crazy too.
Be careful: you may hallucinate the right command to recover the flag!
Unfortunately, the computer is crazy too: every answer is scrambled.
Fortunately, it is crazy just as you are!

author:
Pietro Lepori

public files:
server.py

---

flag:
KSUS{756e6978207374756666}

---

parameters:
As `w` is broken in containers, the `true_server.py` will run instead.
Ideally, the script runs as an unprivileged user, and the root user runs the described command.
That is not strictly necessary, but unintended solutions may be possible.
Be ready to test things in case of tickets.

idea:
On a unix system, what the users are doing is visible to other users.
The `w` command is our target.
It will be a prefix of `step()` on average once every 64 attempts.
A partial solution is to spam `shell 1`, but the answer would not be understandable.
Fortunately, `_memory` never sees the original (empty) `_state`.
So `reset()` will not intercept `seed=""`.
Therefore, we can travel back in time by sending `reset` without arguments when we see a good answer with `step`.
To avoid long runs, we can reset the internal secret after every `step`, triggering a hard reset with `reset`.
Note: Due to difficulties in making `w` work in a container the actual script on the server had a modified `run()`.
The modified function intercepts the first argument `w` and gives the correct answer.
To account for unintended solution the actual `run()` is called in all the other cases.
EDIT: The original script had a bug that could compromise the availability of the challenge.
Therefore it had to be patched during the competition.
Waiting for `sh` instead of `w` provided a blind remote shell, this was because the `input` parameter for `run()` was not set.
