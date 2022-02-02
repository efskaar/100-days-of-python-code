import os

personsAndBids = {}

while True:
  os.system('cls')
  print('Buy my best friend for a hidden price. If you bid the most, you win, but you don\'t know what everybody else bids. \nThis is the silent auction for my best friend \u2665')
  morePeople = input('Write Y to registrer a new bid: ')
  if morePeople.lower() == 'y':
    person = input('Write your name please: ')
    bid = int(input('Write your bid please: '))
    personsAndBids[bid] = person
  else:
    break
os.system('cls')
print('Person       Bid')
for key in personsAndBids.keys():
  print(f'{personsAndBids[key]:9}    {key}')
print()


maxBid = max(personsAndBids.keys())
print(f'The highest bid was {maxBid}$\n{personsAndBids[maxBid]} had the highest bid\n')
     