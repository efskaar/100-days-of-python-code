
depth = 0
binaryTree = [0,[0],[0]]
prettyPrintString = []
printString = ''


def addToBinaryTree(binaryString):
  tempBinaryTreePosition = binaryTree
  for binary in binaryString:
    if binary != '\n':
      tempBinaryTreePosition = tempBinaryTreePosition[int(binary)+1]
      tempBinaryTreePosition[0] += 1
      if len(tempBinaryTreePosition) == 1:
        tempBinaryTreePosition.append([0])
        tempBinaryTreePosition.append([0])

def readFileInput(file):
  with open(file,'r') as infile:
    for line in infile:
      addToBinaryTree(line)

def depthBinaryTree(localBinaryTree,depth):
  if len(localBinaryTree) == 1:
    return
  else:
    depth +=1
    updateDepth(depth)
    depthBinaryTree(localBinaryTree[1],depth)
    depthBinaryTree(localBinaryTree[2],depth)


def updateDepth(newDepth):
  global depth
  depth = newDepth if newDepth>depth else depth

def stringifyBinaryTree(binaryTree):
  global depth
  global printString
  global prettyPrintString
  currentDepth = 1
  while currentDepth < depth:
    recursiveStringifyLevel(binaryTree,currentDepth,0)
    prettyPrintString.append(printString)
    printString = ''
    currentDepth += 1

def recursiveStringifyLevel(binaryTreePrint,printDepth,currentDepth):
  if len(binaryTreePrint) == 1 or currentDepth > printDepth:
    return
  elif currentDepth == printDepth:
    global printString 
    printString += f'{binaryTreePrint[0]} '
  else:
    recursiveStringifyLevel(binaryTreePrint[1],printDepth,currentDepth+1)
    recursiveStringifyLevel(binaryTreePrint[2],printDepth,currentDepth+1)

def rightSidePrintBinaryTree():
  global prettyPrintString
  maxLength = len(prettyPrintString[-1].strip().split(' '))
  for line in prettyPrintString:
    nrInLine = line.strip().split(' ')
    currentLength = len(nrInLine)
    emptyness = int(maxLength/currentLength)-1
    for nr in nrInLine:
      for i in range(emptyness):
        print(' '*4,end='')
      print(nr+(' '*(4-len(nr))),end='')
    print()

def leftSidePrintBinaryTree():
  global prettyPrintString
  maxLength = len(prettyPrintString[-1].strip().split(' '))
  for line in prettyPrintString:
    nrInLine = line.strip().split(' ')
    currentLength = len(nrInLine)
    emptyness = int(maxLength/currentLength)-1
    for nr in nrInLine:
      print(nr+(' '*(4-len(nr))),end='')
      for i in range(emptyness):
        print(' '*4,end='')
    print()

def centralPrintBinaryTree():
  global prettyPrintString
  maxLength = len(prettyPrintString[-1].strip().split(' '))*4
  for line in prettyPrintString:
    nrInLine = line.strip().split(' ')
    partLength = int(maxLength/(len(nrInLine)*2))
    print(' '*partLength,end='')
    for i in nrInLine:
      print(i,end='')
      print(' '*((partLength*2)-len(i)),end='')
    print(' '*partLength,end='')
    print()



readFileInput('006outfile.txt')
depthBinaryTree(binaryTree,0)
stringifyBinaryTree(binaryTree)
rightSidePrintBinaryTree()
leftSidePrintBinaryTree()
centralPrintBinaryTree()