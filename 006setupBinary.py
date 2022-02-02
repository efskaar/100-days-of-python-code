from random import random

with open('011outfile.txt','w') as outfile:
  for i in range(1000):
    for i in range(6):
      outfile.write(str([0,1][random()>0.5]))
    outfile.write('\n')
