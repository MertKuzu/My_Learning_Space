def sumPrime(n):
    sum, sieve = 0,[True]*n
    for p in range(2,n):
        if sieve[p]:
            sum += p
            for i in range(p*p,n,p):
                sieve[i] = False
    return sum

print(sumPrime(2000000))