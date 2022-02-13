graph = {
  'a':['c','b'],
  'b':['d'],
  'c':['e'],
  'd':['f'],
  'e':[],
  'f':[],
}

def depthFirstPrint(graph,source):
  stack = [source]
  while len(stack)>0:
    current = stack[-1]
    stack = stack[:-1:]
    print(current,end=' ')
    for ele in graph[current]:
      stack.append(ele)
  print()

def depthRecursivFirstPrint(graph,source):
  print(source,end=' ')
  if len(graph[source]) > 0:
    for ele in graph[source][::-1]:
      depthRecursivFirstPrint(graph,ele)

def breadthFirstPrint(graph,source):
  stack = [source]
  while len(stack)>0:
    current = stack[0]
    stack = stack[1::]
    print(current,end=' ')
    for ele in graph[current]:
      stack.append(ele)
  print()

depthRecursivFirstPrint(graph,'a')
print()
depthFirstPrint(graph,'a')
breadthFirstPrint(graph,'a')