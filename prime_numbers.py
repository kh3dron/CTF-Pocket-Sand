#all of this works. But I think it can go faster.
#Prime number stuff has to be brute force at some level,
#but surely there's room for optimization.

def generatePrimeString (start, showsProgress):
    result = ""
    while start != 1:
        for x in range (2, 99999999):
            if (showsProgress & (x % 1000000 == 0)):
                print "Checking past " + str(x) + "..."
            if (start % x == 0):
                if (showsProgress):
                    print "Found factor: " + str(x) + ", now parsing " + str(start/x)
                if ((start / x) == 1):
                    result += str(x)
                else:
                    result += str(x) + "x"
                start = start / x
                break
    return result


def isPrime(z):
    return (generatePrimeString(z, False) == str(z))

def numberOfFactors(q):
    return generatePrimeString(q, False).count("x")

print isPrime(11)
print numberOfFactors(11)
