graph={
    'A':['B','C'],
    'B':['A','E','D'],
    'C':[],
    'D': ['B'],
    'E': []
}
visited=set()
def dfs(graph,visited,node):
    if node not in visited:
        print(node, end=" \n")
        visited.add(node)
        for child in graph[node]:
            if child  not in visited:
                    dfs(graph,visited,child)

print("DFS search")
dfs(graph,visited,"A")

