def is_prime(n):
    if n>1:
        for i in range(2,n):
            if (n%i) == 0:
                return False;
        else:
            return True;
    else:
        return False;

if __name__ == "__main__":
    while True:
        x = int(input('> '));
        print(is_prime(x));
