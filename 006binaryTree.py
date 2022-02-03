class BinaryTree():
  def __init__(self):
    self.prettyPrintString = []
    self.binaryTree = [0,[0],[0]]
    self.printString = ''
    self.depth = 0

  def addToBinaryTree(self,binaryString):
    tempBinaryTreePosition = self.binaryTree
    for binary in binaryString:
      if binary != '\n':
        tempBinaryTreePosition = tempBinaryTreePosition[int(binary)+1]
        tempBinaryTreePosition[0] += 1
        if len(tempBinaryTreePosition) == 1:
          tempBinaryTreePosition.append([0])
          tempBinaryTreePosition.append([0])

  def readFileInput(self,file):
    with open(file,'r') as infile:
      for line in infile:
        self.addToBinaryTree(line)

  def depthBinaryTree(self,localBinaryTree,depth):
    if len(localBinaryTree) == 1:
      return
    else:
      depth +=1
      self.updateDepth(depth)
      self.depthBinaryTree(localBinaryTree[1],depth)
      self.depthBinaryTree(localBinaryTree[2],depth)


  def updateDepth(self,newDepth):
    self.depth = newDepth if newDepth>self.depth else self.depth

  def stringifyBinaryTree(self):
    currentDepth = 1
    while currentDepth < self.depth:
      self.recursiveStringifyLevel(self.binaryTree,currentDepth,0)
      self.prettyPrintString.append(self.printString)
      self.printString = ''
      currentDepth += 1

  def recursiveStringifyLevel(self,binaryTreePrint,printDepth,currentDepth):
    if len(binaryTreePrint) == 1 or currentDepth > printDepth:
      return
    elif currentDepth == printDepth:
      self.printString += f'{binaryTreePrint[0]} '
    else:
      self.recursiveStringifyLevel(binaryTreePrint[1],printDepth,currentDepth+1)
      self.recursiveStringifyLevel(binaryTreePrint[2],printDepth,currentDepth+1)

  def rightSidePrintBinaryTree(self):
    prettyPrintString = self.prettyPrintString
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

  def leftSidePrintBinaryTree(self):
    prettyPrintString = self.prettyPrintString
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

  def centralPrintBinaryTree(self):
    prettyPrintString = self.prettyPrintString
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


if '__main__' == __name__:
  bt = BinaryTree()
  bt.readFileInput('006outfile.txt')
  bt.depthBinaryTree(bt.binaryTree,0)
  bt.stringifyBinaryTree()
  bt.rightSidePrintBinaryTree()
  bt.leftSidePrintBinaryTree()
  bt.centralPrintBinaryTree()