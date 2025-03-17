a, b = map(int, input().split())

def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return 0
    return n

def primes_sum(a,b):
    sum = 0
    for i in range(a, b+1):
        sum += is_prime(i)
    return sum

print(primes_sum(a,b))
