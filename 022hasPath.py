from tabnanny import verbose


def depthHasPath(graph,source,target):
  stack = [source]
  while len(stack)>0:
    current = stack[-1]
    if current == target:
      return True
    stack = stack[:-1:]
    for ele in graph[current]:
      stack.append(ele)
  return False

def depthRecursivHasPath(graph,source,target):
  if source == target:
    return True
  elif len(graph[source]) > 0:
    for ele in graph[source][::-1]:
      if depthRecursivHasPath(graph,ele,target):
        return True
  return False

def breadthHasPath(graph,source,target):
  stack = [source]
  while len(stack)>0:
    current = stack[0]
    stack = stack[1::]
    if current == target:
      return True
    for ele in graph[current]:
      stack.append(ele)
  return False

def testHasPaths(verbose = False):
  result = 1
  for source in graph.keys():
    
    print(f'{source}| ',end=' ') if verbose else None
    for target in graph.keys():
      result1 = depthHasPath(graph,source,target)
      result2 = depthRecursivHasPath(graph,source,target)
      result3 = breadthHasPath(graph,source,target)
      thisResult = result1==result2 and result1==result3
      result = result*thisResult
      
      print(target,result1==result2 and result1==result3,end=' ') if verbose else None
    print() if verbose else None
  print(f'Has path test: {bool(result)}') if verbose else None
  return bool(result)

graph = {
  'f':['g','i'],
  'g':['h'],
  'h':[],
  'i':['g','k'],
  'j':['i'],
  'k':[],
}

if __name__ == '__main__':
  testHasPaths(verbose=True)
    