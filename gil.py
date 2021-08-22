#This are some code snippets written for GiL:

import sys
a = []
b = a
print("Number of refrence count for [] (empty list) is : ", sys.getrefcount(a))




# single_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('\n')
print('Time taken in seconds for Single Threaded Programe \t\t\t- ', end - start)



# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print('\n')
print('Time taken in seconds for Multi Threaded ( 2 - Threads )  Programe \t- ', end - start)


# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//4,))
t2 = Thread(target=countdown, args=(COUNT//4,))
t3 = Thread(target=countdown, args=(COUNT//4,))
t4 = Thread(target=countdown, args=(COUNT//4,))

start = time.time()
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
end = time.time()
print('\n')
print('Time taken in seconds for Multi Threaded ( 4 - Threads ) Programe  \t- ', end - start)





print("""
	\n
	Python utilizes something called a Global Interpreter Lock (GIL) to allow Python to simulate concurrency. 
	\nThe basic idea is that the interpreter can only ever utilize a single CPU core. \n
	Threading is acheived by having the interpreter switch to a different thread every n instructions (where n) is typically 100,
	but is set in sys.getcheckinterval() and sys.setcheckinterval(). When C extension code is being executed however, Python has no way of knowing 
	how many ‘instructions’ have passed and thus by default keeps the interpreter lock on for the duration of the extension function.
	So that is meaning of  sys.getcheckinterval()  or sys.setcheckinterval()   
	\n
	""")

import sys
# The interval is by default set to 100 instructions:
print("Interval  sys.getswitchinterval()  \t\t: ",sys.getswitchinterval())
print('The interval is by default set to 100 instructions. that is after 100 instrunection (i.e 0.005) thread aquiring GIL releasee it. \n')
print("\n \nInterval sys.getcheckinterval() \t\t: ",sys.getcheckinterval() )
print('The interval is by default set to 100 instructions. that is after 100 instrunection (i.e 0.005) thread aquiring GIL releasee it. \n')



from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
	print('\n------------------------------------------------------------------------------------------------------------\n')
	start0 = time.time()
	countdown(COUNT)
	end0 = time.time()
	print('\n\nTime taken in seconds in the case of Single - Processing (One Process )\t-', end0 - start0)
	pool = Pool(processes=2)
	start = time.time()
	r1 = pool.apply_async(countdown, [COUNT//2])
	r2 = pool.apply_async(countdown, [COUNT//2])
	pool.close()
	pool.join()
	end = time.time()
	print('\n\nTime taken in seconds in the case of Multi - Processing (Two Processess )\t-' , end - start)
	pool = Pool(processes=4)
	start = time.time()
	r1 = pool.apply_async(countdown, [COUNT//4])
	r2 = pool.apply_async(countdown, [COUNT//4])
	r3 = pool.apply_async(countdown, [COUNT//4])
	r4 = pool.apply_async(countdown, [COUNT//4])
	pool.close()
	pool.join()
	end = time.time()
	print('\n\nTime taken in seconds in the case of Multi - Processing (Four Processess )\t-' , end - start)
	print('\n------------------------------------------------------------------------------------------------------------\n')
