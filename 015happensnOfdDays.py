from numpy import * 
from random import * 
from collections import * 
'''
If you live at a student home x days a year with n other people
How many of the days can you expect a thing to happen if each person does it onces a year.
'''

dict_ant =  {}
for i in range(10):	
	days = 200
	dates = zeros(days)
	nPersons = 200
	nTimes = 1
	for i in range(nPersons):
		for j in range(nTimes):
			dates[randint(0,days-1)] += 1
	dict_ant.update(Counter(dates))

print('Nr Of People ',end='')
for key in sorted(dict_ant.keys()):
	print(f'{int(key):-3} ',end="")

print()
print('Nr Of Days   ',end='')
for key in sorted(dict_ant.keys()):
	print(f'{int(dict_ant[key]):-3} ',end="")