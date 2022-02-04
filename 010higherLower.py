from higherLowerData import * 
from higherLowerArt import * 
from random import random
import os
import keyboard

def randomIndex(currentIndex):
  newIndex = int(random()*len(data))
  while currentIndex == newIndex:
    newIndex = int(random()*len(data))
  return newIndex

def writeOutItem(index):
  print(f'{data[index]["name"]}')
  print(f'{data[index]["country"]}')
  print(f'{data[index]["description"]}')

def writeFollowersAndName(index):
  print(f'{data[index]["name"]} has {data[index]["follower_count"]}M followers')

def waitForInput(allowedKeys):
    keyPressed = keyboard.read_key()
    while keyPressed not in allowedKeys:
      keyPressed = keyboard.read_key()
    return keyPressed


def game():
  print(logo)
  print('Press Enter to start or ESC to exit')
  while waitForInput(['esc','enter']) == 'enter':
    score = 0
    alive = True
    oldItem = randomIndex(-1)
    while alive:
      os.system('cls')
      #get an opponent
      newItem = randomIndex(oldItem)
      
      #write out challange
      writeOutItem(oldItem)
      print(vs)
      writeOutItem(newItem)
      #options are specified for the user
      print(f'\nPress W if you think the last has fewer followers')
      print(f'Press S if you think the last has more followers')

      #wait for user to choose one of the two
      playerInput = waitForInput(['w','s'])

      #pick out the choice 
      bothFollowersCount = [data[oldItem]["follower_count"],data[newItem]["follower_count"]]
      choiceFollowers = bothFollowersCount[playerInput == 's']
      print('')
      writeFollowersAndName(oldItem)
      writeFollowersAndName(newItem)
      
      if choiceFollowers != max(bothFollowersCount):
        alive = False
        print(f'\nGame Over! You reached a score of {score}\n')
      else:
        score += 1
        oldItem = newItem
        print(f'\nYou are correct! You now have {score} points\n')
        print('Press Enter to continue:')
        waitForInput(['enter'])
    print('\nEnter for play again\nESC for exit')
  

if '__main__' == __name__:
  game()