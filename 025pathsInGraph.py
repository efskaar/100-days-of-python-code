
def edgesToGraph(edges):
  graph = {}
  for edge in edges:
    v1,v2 = edge
    graph[v1] = [] if v1 not in graph.keys() else graph[v1]
    graph[v2] = [] if v2 not in graph.keys() else graph[v2]
    graph[v1].append(v2)
    graph[v2].append(v1)
  return graph

def recursiveUndirectedHasPath(edges):
  graph = edgesToGraph(edges)
  paths = []
  visited = []
  for vertice in graph.keys():
    if vertice not in visited:
      visited.append(vertice)
      paths.append(depthRecursivHasPath(graph,vertice,[vertice],visited))
  return paths

def depthRecursivHasPath(graph,current,path,visited):
  if len(graph[current]) > 0:
    for vertice in graph[current][::-1]:
      if vertice not in path:
        visited.append(vertice)
        path.append(vertice)
        depthRecursivHasPath(graph,vertice,path,visited)
  return path

def largestComponent(edges):
  paths = recursiveUndirectedHasPath(edges)
  index = -1
  maxLength = -1
  for i in range(len(paths)):
    if len(paths[i]) > maxLength:
      maxLength = len(paths[i])
      index = i
  return paths[index]


edges =[
   ['i','j'],
   ['i','k'],
   ['m','k'],
   ['l','k'],
   ['o','n'],
   ]

if __name__ == '__main__':
  print(recursiveUndirectedHasPath(edges))
  print(largestComponent(edges))