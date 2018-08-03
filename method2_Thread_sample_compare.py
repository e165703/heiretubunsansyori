import concurrent.futures, time
import math

p=1112941
q=1128601

n = p*q
separate = 7

def func1():
    start2 = time.time()
    
    #print("スレッド1お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int(1)
    end = int(start + root_n/separate)
    for i in range(start,end):
        if(i != 1 and n%i == 0):
            print("thread1" +  "p = " + str(i))
            print("thread1" + "q = " + str(n/i))
    #print("スレッド1終了")
    end2 = time.time()
    #print('1実行時間:{}'.format(end2 - start2))

def func2():
    start2 = time.time()
    
    #print("スレッド2お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int((root_n/7)*(1) + 1)
    end = int(start + root_n/separate)
    for	i in range(start,end):
        if(i != 1 and n%i == 0):
            print("thread1" +  "p = " + str(i))
            print("thread1" + "q = " + str(n/i))
    #print("スレッド2終了")
    end2 = time.time()
    #print('2実行時間:{}'.format(end2 - start2))

def func3():
    start2 = time.time()
    
    #print("スレッド3お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int((root_n/7)*(2) + 1)
    end = int(start + root_n/separate)
    for i in range(start,end):
        if(i != 1 and n%i == 0):
            print("p = " + str(i))
            print("q = " + str(n/i))
    #print("スレッド3終了")
    end2 = time.time()
    #print('3実行時間:{}'.format(end2 - start2))
    
def func4():
    start2 = time.time()
    
    #print("スレッド4お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int((root_n/7)*(3) + 1)
    end = int(start + root_n/separate)
    for i in range(start,end):
        if(i != 1 and n%i == 0):
            print("p = " + str(i))
            print("q = " + str(n/i))
    #print("スレッド4終了")
    end2 = time.time()
    #print('4実行時間:{}'.format(end2 - start2))

def func5():
    start2 = time.time()
    
    #print("スレッド5お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int((root_n/7)*(4) + 1)
    end = int(start + root_n/separate)
    for i in range(start,end):
        if(i != 1 and n%i == 0):
            print("p = " + str(i))
            print("q = " + str(n/i))
    #print("スレッド5終了")
    end2 = time.time()
    #print('5実行時間:{}'.format(end2 - start2))

def func6():
    start2 = time.time()
    
    #print("スレッド6お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int((root_n/7)*(5) + 1)
    end = int(start + root_n/separate)
    for i in range(start,end):
        if(i != 1 and n%i == 0):
            print("p = " + str(i))
            print("q = " + str(n/i))
    #print("スレッド6終了")
    end2 = time.time()
    #print('6実行時間:{}'.format(end2 - start2))
    
def func7():
    start2 = time.time()
        
    #print("スレッド7お仕事開始")
    root_n = int(math.floor(math.sqrt(n)))
    start = int((root_n/7)*(6) + 1)
    end = int(start + root_n/separate)
    for i in range(start,end):
        if(i != 1 and n%i == 0):
            print("p = " + str(i))
            print("q = " + str(n/i))
    #print("スレッド7終了")
    end2 = time.time()
    #print('7実行時間:{}'.format(end2 - start2))
    

if __name__ == "__main__":
    start = time.time()
    executor = concurrent.futures.ProcessPoolExecutor(max_workers=1)
    executor.submit(func1)
    executor.submit(func2)
    executor.submit(func3)
    executor.submit(func4)
    executor.submit(func5)
    executor.submit(func6)
    executor.submit(func7)
    executor.shutdown()
    end = time.time()
    print(end-start)



    
