lifes = 6
word = 'Erik Skaar'
lettersToGuess = [char.lower() for char in word]
revealLetters = ['_' if char != ' ' else ' ' for char in word]

def printCurrentState():
  print('\n')
  if lifes == 0:
    endOfGame('Game Over \U0001F571')
  elif '_' not in revealLetters:
    endOfGame('You Won \u2606')
  else:
    print(f'Number of lifes left: ',end='')
    for i in range(lifes):
      print('\u2665 ',end='')
    print('')
    for char in revealLetters:
      print(char,end=' ')
    print('\n')

def endOfGame(text):
  print(text)
  print('')
  for char in word:
    print(char,end='')
  print('\n')

while '_' in revealLetters and lifes > 0:
  printCurrentState()
  guessLetter = input('Guess a letter: ').lower()
  if (guessLetter in lettersToGuess):
    for i in range(len(revealLetters)):
      revealLetters[i] = word[i] if guessLetter == lettersToGuess[i] else revealLetters[i]
  else:
    lifes -= 1

printCurrentState()