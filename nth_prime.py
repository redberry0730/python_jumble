def nth_prime(n):
    prime = 1;
    count = 1;
    if n == 1:
        return 2;
    while count<n:
        prime = prime+2;
        if is_prime(prime)==True:
            count = count+1;
    return prime;

def is_prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                return False;
        else:
            return True;

if __name__ == "__main__":
    while True:
        x = int(input('> '));
        print(nth_prime(x));