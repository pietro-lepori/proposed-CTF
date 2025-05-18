name:
Lightning Fast Scrambling?

description:
Marvel at my new super-fast cipher!
It even provides a message integrity check :)
Here is my challenge:
VERY/Rjwj1U4DQZ/zyyHxSsMY1iYuOZHs//qWPVYInUz/5cxidrFCrSqco4bbVLpWjHHI4Z+JZOwOfsT#SUS/PDQPS4DlVum2aO+5+SuczHag7/rnYMBUr+pEqEU=
I'm sure you won't be able to recover the passphrase

author:
Pietro Lepori

public files:
lfs.py
challenge.txt

---

flag:
KSUS{6c6673725f6172655f6e6f745f7365637572653038363834363137}

---

parameters:
(chosen to start the 2 parts of the challenge with VERY/ SUS/)
secret > lfsr_are_not_secure08684617
passphrase > 293590124198353963520497

idea:
The name reads LFS? and this is just a LFSR where you have to guess the last part of the key.
The LFSR works 8 bits per step and the key is the first 8 bytes of the produced keystream.
The plaintext is the flag and begins with "KSUS{" this gives 5 bytes of the key.
The remaining 3 bytes can be bruteforced.
The easy way is to exploit the low entropy of the rest of the flag (hex digits: 4 bits per byte), at most 4096 attempts are required.
It is indeed not possible to recover the passphrase but it doesn't matter :)
