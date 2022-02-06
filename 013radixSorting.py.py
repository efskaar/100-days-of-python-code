from numpy import random
import time

liste = random.randint(1,10000,1000000)
def radix(liste,i,maxI):
	if i > maxI: return liste;
	digits = [[] for i in range(10)]
	for val in liste:
		digits[val%(10*i)//i].append(val)
	liste = [val for d in digits for val in d]
	return radix(liste,i*10,maxI)

t1 = time.time()
radix(liste,1,10**len(str(max(liste))))
print(time.time()-t1)