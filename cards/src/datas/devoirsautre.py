def isPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def primeFactors(n):
    if isPrime(n):
        return [n]
    else:
        factors = []
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                n //= i
                factors.append(i)
        if n > 1:
            factors.append(n)
        return factors
    
print(primeFactors(18))