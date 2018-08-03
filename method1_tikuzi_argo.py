import time

def prime3():
    counter = 0
    primes = [2, 3]
    start = time.time()
    for n in range(5, 100000, 2):
        isprime = True
        for i in range(1, len(primes)):
            counter += 1
            if primes[i] ** 2 > n:
                break
            counter += 1
            if n % primes[i] == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)
    elapsed_time = time.time() - start
    #print (primes, len(primes))
    print (elapsed_time)
prime3()
