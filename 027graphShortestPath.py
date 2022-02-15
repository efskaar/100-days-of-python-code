
def edgesToGraph(edges):
  graph = {}
  for edge in edges:
    v1,v2 = edge
    graph[v1] = [] if v1 not in graph.keys() else graph[v1]
    graph[v2] = [] if v2 not in graph.keys() else graph[v2]
    graph[v1].append(v2)
    graph[v2].append(v1)
  return graph

def breadthShortestPath(edges,source,target):
  graph = edgesToGraph(edges)
  visited = [source]
  stack = [[source,0]]
  while len(stack)>0:
    current = stack[0]
    stack = stack[1::]
    if current[0] == target:
      return current[1]
    for ele in graph[current[0]]:
      if ele not in visited:
        visited.append(ele)
        stack.append([ele,current[1]+1])
  return -1

edges =[
   ['i','j'],
   ['i','k'],
   ['m','k'],
   ['l','k'],
   ['o','n'],
   ]

if __name__ == '__main__':
  print(breadthShortestPath(edges,'i','l'))