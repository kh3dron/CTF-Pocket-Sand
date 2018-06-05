#Just some little stuff, add mroe if needed

def primeFactors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def isPrime(numb):
    return len(primeFactors(numb)) == 1


for x in range (0, 9999):
    print isPrime(x)
