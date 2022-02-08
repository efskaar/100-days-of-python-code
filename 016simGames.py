import random
from numpy import * 


nSim = 100
nGames = 1000
nGamesStreak = 100

print(random.randint(0, 2))

winrates = linspace(0,0,nGamesStreak+1)
for s in range(nSim):
  kamper = []
  for i in range(nGames):
    kamper.append(random.randint(0,2))
  for i in range(nGames-nGamesStreak):
    summen = sum(kamper[i:i+nGamesStreak:])
    winrates[summen] += 1


for i in range(len(winrates)):
  print(i,winrates[i]/nSim)
print(sum(winrates))