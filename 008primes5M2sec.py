from numpy import concatenate,where,ones,array
import time

def find_primes(primes,length=100):
	pot_primes = ones(int(length))
	pot_primes[0] = 0
	for i in range(len(primes)):
		pot_primes[primes[i]::primes[i]] = 0
	new_primes = where(pot_primes == 1)[0][1:]
	return concatenate((primes,new_primes))

if __name__ == '__main__':
	t0 = time.time()
	primes = array([2,3,5,7])
	for i in [2,4,8]:
		primes = find_primes(primes,10**i)
		print(10**i,time.time()-t0,len(primes))

# with open('006-5M-primes.txt','w') as outfile:
#   for i in range(len(primes)):
#     outfile.write(f'{i} {primes[i]}\n')