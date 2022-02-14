

def edgesToGraph(edges):
  graph = {}
  for edge in edges:
    v1,v2 = edge
    graph[v1] = [] if v1 not in graph.keys() else graph[v1]
    graph[v2] = [] if v2 not in graph.keys() else graph[v2]
    graph[v1].append(v2)
    graph[v2].append(v1)
  return graph

def depthUndirectedHasPath(edges,source,target):
  graph = edgesToGraph(edges)
  visitedVertices = [source]
  stack = [source]
  while len(stack)>0:
    current = stack[-1]
    if current == target:
      return True
    stack = stack[:-1:]
    for ele in graph[current]:
      if ele not in visitedVertices:
        visitedVertices.append(ele)
        stack.append(ele)
  return False

def recursiveUndirectedHasPath(edges,source,target):
  graph = edgesToGraph(edges)
  return depthRecursivHasPath(graph,source,target,[source])

def depthRecursivHasPath(graph,source,target,visited):
  if source == target:
    return True
  elif len(graph[source]) > 0:
    for ele in graph[source][::-1]:
      if ele not in visited:
        visited.append(ele)
        if depthRecursivHasPath(graph,ele,target,visited):
          return True
  return False


edges =[
   ['i','j'],
   ['i','k'],
   ['m','k'],
   ['l','k'],
   ['o','n'],
   ]

if __name__ == '__main__':
  print(depthUndirectedHasPath(edges,'i','n'))
  print(recursiveUndirectedHasPath(edges,'i','n'))