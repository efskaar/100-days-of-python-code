
def findIslands(grid):
  visited = []
  islands = []
  for r_i in range(len(grid)):
    for c_i in range(len(grid[r_i])):
      island = searchForIsland(grid,(r_i,c_i),visited)
      if len(island) > 0:
        islands.append(island)
  return islands

def searchForIsland(grid,cord,visited):
  if cord in visited or grid[cord[0]][cord[1]] == 0:
    return []
  else:
    island = []
    stack = [cord]
    while len(stack) > 0:
      current = stack[-1]
      stack = stack[:-1:]
      if current not in visited and grid[current[0]][current[1]] != 0:
        island.append(current)
        visited.append(current)
        addToStack(grid,current,stack)
    return island

def addToStack(grid,pos,stack):
  if pos[0] > 0:
    stack.append((pos[0]-1,pos[1]))
  if pos[0] < len(grid)-1:
    stack.append((pos[0]+1,pos[1]))
  if pos[1] > 0:
    stack.append((pos[0],pos[1]-1))
  if pos[1] < len(grid[pos[0]])-1:
    stack.append((pos[0],pos[1]+1))
    
def findSmallestIsland(grid,verbose=False):
  islands = findIslands(grid)
  maxLength = len(islands[0])
  index = 0
  for i in range(len(islands)):
    if len(islands[i]) < maxLength:
      index = i
      maxLength = len(islands[i])
  print(f'Smallest island is {islands[index]} with a length of {len(islands[index])}') if verbose else None
  return islands[index]

def findLargestIsland(grid,verbose=False):
  islands = findIslands(grid)
  maxLength = -1
  index = -1
  for i in range(len(islands)):
    if len(islands[i]) > maxLength:
      index = i
      maxLength = len(islands[i])
  print(f'Largest island is {islands[index]} with a length of {len(islands[index])}') if verbose else None
  return islands[index]


grid = [[0,1,0,0,0],
        [0,1,0,0,0],
        [0,0,0,1,0],
        [0,0,1,1,0],
        [1,0,0,1,1],
        [1,1,0,0,0],]

if __name__ == '__main__':
  findIslands(grid)
  findSmallestIsland(grid,verbose=True)
  findLargestIsland(grid,verbose=True)