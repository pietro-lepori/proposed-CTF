name:
key in the big haystack

description:
Have you found the previous key? Well done!
(If not, solve "key in the haystack" first.)
Now the haystack is bigger: you'll need a good metal detector :D
I know a quite sophisticated trick that recovers the key in seconds, from the small haystack.
The same trick works now, but requires a few hours.
Don't despair: with a good idea you'll find it in less than 5'.

author:
Pietro Lepori

public files:
challenge.py
big_output.txt

___

flag:
KSUS{43525420697320612076657279206e69636520747269636b}

---

parameters:
N/A

idea:
Same as before (gcd between the polynomial and its derivative), but a simple Euclidean algorithm is too slow.
A solution could have been binary search for the zeros.
But this time non-double solution are pairwise at distance 2 so a negative value is difficult to find.
Increasing / decreasing could be used instead of positive / negative.
That just means binary search on the derivative: we are interested to solutions that are an odd integer.
Newton's method may also be a usefool tool (do integer divisions; floats are bad here).
The attached solver uses a different approach that makes the original idea competitive again.
We can compute the same polynomial gcd, but over finite fields Z/pZ, for some primes p.
The primes should be big, so the product is over 2**1024 - the infinity norm of (x + p) * (x + q) - with only a few primes (and few gcd computations).
The primes should be small, so that the operations with big nums are not expensive.
A good compromise is to take the 19 biggest primes less than 2**63 (taking only 17 is enough).
Then the second-degree polynomial can be recovered by Chinese Reminder Theorem, using the extended Euclidean algorithm for integers.
