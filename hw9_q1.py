import random
import math
import sys
sys.setrecursionlimit(2500)

def extended_euclid(n1, n2):
    if n1 == 0:
        return (n2, 0, 1);
    else:
        (q, r) = divmod(n2, n1);
        (a, b, d) = extended_euclid(r, n1);
        return (a, d - q * b, b);

a, b = random.randint(pow(10, 1000),pow(10, 1001)), random.randint(pow(10, 1000),pow(10, 1001));
g, x, y = extended_euclid(a, b);
print("gcd(", a , "," , b, ") = ", g);
print("(", x, "*", a, ")", "+", "(", y, "*", b, ")", "=", g);


def fermatTest(n, ntrials):
    b = n - 1;
    a = random.randint(2, b);
    if pow(a, b, n) != 1:
        return False;
    else:
        if ntrials > 0:
            return fermatTest(n, ntrials - 1);
        else:
            return True;

def fermatPrime(max, ntrials):
    n = random.randint(2, max);
    if n == 2:
        return n;
    test = fermatTest(n, ntrials);
    if test == True:
        return n;
    else:
        return fermatPrime(max, ntrials);

print(fermatPrime(150, 5))







