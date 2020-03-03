# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
#Universidad Autónoma de Chihuahua
# Facultad de Ingeniería
# Sistemas de Búsqueda y Razonamiento 
# Equipo: 
#   Carlos García
#   Alejandro Aguirre
#   Ericka Bermúdez

# referencias: https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python


# %%
graph = {
        'A':['E','D','C', 'B'], 
        'B':['H','C','A'], 
        'C':['H','G','D','B','A'],
        'D':['G','F','E', 'C', 'A'], 
        'E':['F','D','A'], 
        'F':['G','E', 'D', 'C'],
        'G':['F', 'C'],
        'H':['C', 'B']
        }


# %%
import numpy as np


# %%
visited = [] 
queue = []
parents = {}


# %%
def subt(queue, visited): 
    for item in queue: 
        for item2 in visited: 
            if item == item2:
                queue.remove(item)
    return queue


# %%
def dfs(visited, graph, node, parent, goal):
    print("-----------------------")
    print("ACTUAL: ", node)
    
    if node not in visited and node != goal:
        visited.append(node)
        
        for child in graph[node]:
            if child not in visited and child not in queue:
                queue.append(child)
                parents[child] = node
        nextItem = subt(queue, visited)

        nextId = len(nextItem)-1
        nextNode = nextItem[nextId]
        print("ABIERTOS: ", queue)
        print("CERRADOS: ", visited)
        dfs(visited, graph, nextNode, node, goal)


# %%
#[parent, child]
parents['G']='G'
dfs(visited, graph, 'G', 'G', 'B')
visited.append('B')


# %%
visited


# %%
queue = queue[0:len(queue)-1]
queue


# %%
parents


# %%
def getPath(visited,parents):
    path=[]
    aux = visited[len(visited)-1]
   
    while(aux != parents.get(aux)):
        path.append(aux)
        aux = parents.get(aux)
    path.append(aux)
    path.reverse()
    print('El camino es:')
    print(path)
getPath(visited,parents)

