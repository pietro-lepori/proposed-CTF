name:
key in the haystack

description:
I've encrypted my secret message with RSA.
Easy stuff, right?
Well, I'm not giving you the key outright...
I've hidden it in a haystack!
Sure, a key is not a needle, and this haystack is not that big.
It shouldn't take more than 10' to find it, if you have an half-decent metal detector.
Good luck!

author:
Pietro Lepori

public files:
challenge.py
output.txt

___

flag:
KSUS{6465726976617469766573206172652061206e69636520747269636b}

---

parameters:
N/A

idea:
The haystack is just a polynomial: product of (x + p) over p random primes.
The RSA factors are the only (not necessarily, but quite surely) repeated roots of the polynomial.
The gcd of the polynomial with its derivative will be (x + p) * (x + q), where p and q are the factors.
This allows us to recover both the modulus and the private exponent.
Alternatively, one could find all the roots and try their pairwise combinations to decrypt.
That may be feasible, but - having the "accidentally" repeated roots - it's not necessary.
Care must be taken in computing the gcd: floats don't have enough range, and fractions may be too slow.
