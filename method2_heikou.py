from multiprocessing import Process, Manager
import time
import math
import concurrent.futures
manager = Manager()
primes = manager.list([])
n = 70000
p = 131
q = 239
w = p*q
def prime_num_1():
     primes1 = []
     range_first = 1
     range_end = int(range_first + n/7)
     #print("process1:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process1:end")
     #print(primes1)
def prime_num_2():
     primes2 = []
     range_first = int((n/7)*(1) + 2)
     range_end = int(range_first + n/7)
     #print("process2:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process2:end")
     #print(primes2)
def prime_num_3():
     primes3 = []
     range_first = int((n/7)*(2) + 2)
     range_end = int(range_first + n/7)
     #print("process3:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process3:end")
     #print(primes3)
def prime_num_4():
     primes4 = []
     range_first = int((n/7)*(3) + 2)
     range_end = int(range_first + n/7)
     #print("process4:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process4:end")
     #print(primes4)
def prime_num_5():
     primes5 = []
     range_first = int((n/7)*(4) + 1)
     range_end = int(range_first + n/7)
     #print("process5:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process5:end")
     #print(primes5)
def prime_num_6():
     primes6 = []
     range_first = int((n/7)*(5) + 1)
     range_end = int(range_first + n/7)
     #print("process6:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process6:end")
     #print(primes6)
def prime_num_7():
     start = time.time()
     primes7 = []
     range_first = int((n/7)*(6) + 1)
     range_end = int(range_first + n/7)
     #print("process7:start")
     for p in range(range_first,range_end):
        isprime = True
        for i in range(2, p):
            if p % i == 0:
                isprime = False
                break
        if isprime:
            primes.append(p)
     #print("process7:end")
     end = time.time()
     #print(primes)
     print(end-start)
if __name__ == "__main__":
        executor = concurrent.futures.ProcessPoolExecutor(max_workers=7)
        executor.submit(prime_num_1)
        executor.submit(prime_num_2)
        executor.submit(prime_num_7)
        executor.submit(prime_num_3)
        executor.submit(prime_num_4)
        executor.submit(prime_num_5)
        executor.submit(prime_num_6)
        executor.shutdown()
        #print(primes)
        for i in range(len(primes)-1):
             if w % primes[i] == 0 and primes[i] != 1:
                 print("p = " + str(primes[i]))
                 print("q = " + str(int(w/primes[i])))
                 break
            
            
