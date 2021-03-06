def recursive_dfs(graph, start, path=[]):
  
  path=path+[start]
  for node in graph[start]:
    if not node in path:
      path=recursive_dfs(graph, node, path)
  return path

def iterative_dfs(graph, start, path=[]):

  q=[start]
  while q:
    v=q.pop(0)
    if v not in path:
      path=path+[v]
      q=graph[v]+q
  return path

def iterative_bfs(graph, start, path=[]):
  
  q=[start]
  while q:
    v=q.pop(0)
    if not v in path:
      path=path+[v]
      q=q+graph[v]
  return path


graph = {'A':['B','C'],'B':['D','E'],'C':['D','E'],'D':['E'],'E':['A']}
print('recursive dfs', recursive_dfs(graph, 'A'))
print('iterative dfs', iterative_dfs(graph, 'A'))
print('iterative bfs', iterative_bfs(graph, 'A'))
