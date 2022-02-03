from numpy import random as nRandom
from random import random
import time

'''
comparision between binary search and a binary search with a linear approximation for the first x tries
The result is dependent on the length of the list and how many tries the linear approximation does
For 3 tries and length 100'000, the linear approx seems to be 5-15% faster
'''


def binarySearch(value,numbers,maxTries=20):
	'''
	Parameters:
		array numbers 	- needs to be a sorted list  
		float value			- value in the list
		Optional:
			int maxTries	- tries before the algoritm stops
	return:
		int nI - index in list - NaN if an index was not found within the maxTries
	'''
	tries = 0
	indices = [0,len(numbers)]
	newIndex = int((indices[0]+indices[1])/2)
	while numbers[newIndex] != value:
		if tries > maxTries:
			return None
		indices[int(numbers[newIndex]>value)] = newIndex
		newIndex = int((indices[0]+indices[1])/2)
		tries += 1
	return newIndex

def linaerApproxSearch(value,numbers,maxTries=20):
	'''
	Parameters:
		array numbers 	- needs to be a sorted list  
		float value			- value in the list
		Optional:
			int maxTries	- tries before the algoritm stops
	return:
		int nI - index in list - NaN if an index was not found within the maxTries
	'''
	tries = 0
	i = [0,len(numbers)-1]
	d = (numbers[i[1]]-numbers[i[0]])
	nI = int(i[1]*(value-numbers[i[0]])/d)
	while numbers[nI] != value:
		if tries > maxTries:
			return None
		elif tries < 3:
			i[int(numbers[nI]>=value)] = nI
			d = (numbers[i[1]]-numbers[i[0]])
			nI = int((i[1]-i[0])*(value-numbers[i[0]])/d)+i[0]
		else:
			i[int(numbers[nI]>value)] = nI
			nI = int((i[0]+i[1])/2)
		tries += 1
	return nI


def testFunc(name,func,numbers,attempts):
	'''
	Speed test for the two algorithms
	'''
	t1 = time.time()
	for i in range(attempts):
		findIndex = int(random()*len(numbers))
		func(numbers[findIndex],numbers)
	t2 = time.time()
	print(f'{name} toke {t2-t1:.2f} sec')


if '__main__' == __name__:
	size = int(1e5)
	numbers = nRandom.rand(size)*size
	numbers.sort()
	attempts = 100000
	testFunc('Binary',binarySearch,numbers,attempts)
	testFunc('Linear',linaerApproxSearch,numbers,attempts)
