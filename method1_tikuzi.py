import time
def prime1():
    counter = 0
    primes = []
    start = time.time()
    for n in range(2, 100001):
        isprime = True
        for i in range(2, n):
            counter += 1
            if n % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(n)
    end = time.time()
    print(end-start)
if __name__ == "__main__":
    prime1()
