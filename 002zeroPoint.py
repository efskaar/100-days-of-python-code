from random import random
#def a function that you want to find the zero-point for
def f(x):
  return x**3-x*2+x-1

#pick a and b so f(a) and f(b) is positive and negative, respectively
a = random()*100 - 50
b = random()*100 - 50

#choose a accuracy for the x-value of the zero point
accuracy = 0.0001

#this makes sure that f(a) and f(b) has opposite signs
while (f(a)*f(b)>0):
  a = random()*100 - 50

#this simplifies the if-tests in the while loop
if f(a) < 0:
  a,b = b,a

iteration = 0
while abs(a-b) > accuracy:
  iteration += 1
  m = (a+b)/2 #mid point
  if f(m) > 0:
    a = m
  else:
    b = m
  
print(f'It toke {iteration} iterations to find the zero point to a {accuracy} accuracy')
print(f'\nzero point --> ({a:.3f},{f(a):.2f})\n')
