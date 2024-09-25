import random 
'''
    Graph State Object
'''

from graph_state_generation.graph_state import graph_state

def GraphNoAdjacencies(n_vertices : int):
    graph = graph_state.GraphState(n_vertices)
    return graph


def GraphDisconnectedBipartied(n_vertices : int):
    graph = graph_state.GraphState(n_vertices)
    for i in range(0, n_vertices - 1, 2):
        graph.append(i, i + 1) 

    return graph

def GraphBinaryTree(n_vertices : int):
    graph = graph_state.GraphState(n_vertices)
    for i in range(n_vertices):
        if i != i // 2:
            graph.append(i, i // 2) 
    return graph

def GraphRandom(n_vertices : int, density : float): 
    pass

def GraphComplete(n_vertices : int):
    graph = graph_state.GraphState(n_vertices)
    lst = list(range(n_vertices))
    for i in range(n_vertices):
            graph[i].append(lst[:i], lst[i + 1:]) 
    return graph

