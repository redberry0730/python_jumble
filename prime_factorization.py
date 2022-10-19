def prime_factorization(n):
    numbers = [];
    if n>1:
        for i in range(2,n+1):
            while (n%i)==0:
                n = n/i;
                numbers.append(i);
    return numbers;

if __name__ == "__main__":
    while True:
        x = int(input('> '));
        print(prime_factorization(x));