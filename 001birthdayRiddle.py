"""
You are xy years old. While an other person is yx years old. 
Where x and y are digit in a combined number, e.g. x = 1 and y = 2 ==> you are 12 years old.

Next year the other person will be twice as old as your are now.
How old are you? 
"""
for m in range(1,10,1):       #m for multiple times older
  for f in range(1,10,1):     #f for years in the Future
    for x in range(0,10,1):   #x from the riddle
      for y in range(0,10,1): #y from the riddle
        if (int(str(x)+str(y))*m == int(str(y)+str(x))+f):
          print(f'{m} times older in {f} years --> {x}{y}') 

"""
output: 
1 times older in 9 years --> 10
1 times older in 9 years --> 21
1 times older in 9 years --> 32
1 times older in 9 years --> 43
1 times older in 9 years --> 54
1 times older in 9 years --> 65
1 times older in 9 years --> 76
1 times older in 9 years --> 87
1 times older in 9 years --> 98
2 times older in 1 years --> 37
2 times older in 3 years --> 12
2 times older in 4 years --> 49
2 times older in 6 years --> 24
2 times older in 9 years --> 36
3 times older in 1 years --> 14
3 times older in 2 years --> 28
3 times older in 8 years --> 13
3 times older in 9 years --> 27
4 times older in 3 years --> 16
4 times older in 9 years --> 15
5 times older in 4 years --> 19
5 times older in 9 years --> 18
"""