import random
import numpy as np
import time
import os

'''
Can I make the terminal to a function animator? 
The answer is yes. Yes, I can :) 
Any function of t and x can be animated
'''

#stopp determines the x-axis length from origo 
#1.5*stopp determines the y-axis length from origo
symbol = "X"; start = 0; stopp = 20; 	
x = np.linspace(0,5*np.pi,stopp*10)
def func(x,t):
	return (stopp*0.7)+(stopp*0.8)*np.sin(x/(stopp*0.2)+t)*np.sin(x+t)

for t in x:
	os.system('cls')
	x_sort = np.linspace(start,stopp,5*(stopp)+1)
	y_sort = np.around(func(x_sort,t))
	for j in range(int(1.5*stopp),0,-1):
		indices = [i for i, y in enumerate(y_sort) if y == j]
		linje = "|    "+"     "*stopp
		for x_pos in indices:
			x_ = x_sort[x_pos]
			linje = linje[:int((x_)*5)]+symbol+linje[int((x_)*5)+1:]
		print("%-3d" % j,linje,sep="")

	print("   0-"+"---|-"*(stopp),"\n        ",end="")
	for i in range(1,stopp+1):
		print("%-5d"%i,end="")
	print()
	time.sleep(0.005)