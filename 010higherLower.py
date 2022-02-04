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
  score = 0
  alive = True
  oldItem = randomIndex(-1)
  while alive:
    os.system('cls')
    print(logo)
    print('Guess if the last has higher or lower follower count than the first:\n')
    #get an opponent
    newItem = randomIndex(oldItem)
    
    #write out challange
    writeOutItem(oldItem)
    print(vs)
    writeOutItem(newItem)
    #options are specified for the user
    print(f'\nPress ESC if you think the last is lower')
    print(f'Press Space if you think the last is higher')

    #wait for user to choose one of the two
    playerInput = waitForInput(['esc','space'])

    #pick out the choice 
    bothFollowersCount = [data[oldItem]["follower_count"],data[newItem]["follower_count"]]
    choiceFollowers = bothFollowersCount[playerInput == 'space']
    
    writeFollowersAndName(oldItem)
    writeFollowersAndName(newItem)
    
    if choiceFollowers != max(bothFollowersCount):
      alive = False
      print(f'\nGame Over! You reached a score of {score}')
      return
    score += 1
    oldItem = newItem
    input('Press Enter to continue:')

if '__main__' == __name__:
  game()
  print('\nEnter for play again\nESC for exit')
  while waitForInput(['esc','enter']) == 'enter':
    game()
    print('\nEnter for play again\nESC for exit')