
def edgesToGraph(edges):
  graph = {}
  for edge in edges:
    for i in range(len(edge)):
      v = edge[i]
      graph[v] = [] if v not in graph.keys() else graph[v]
      graph[v].append(edge[(i+1)%2])
  return graph

edges =[
   ['i','j'],
   ['i','k'],
   ['m','k'],
   ['l','k'],
   ['o','n'],
   ]

if __name__ == '__main__':
  print(edgesToGraph(edges))