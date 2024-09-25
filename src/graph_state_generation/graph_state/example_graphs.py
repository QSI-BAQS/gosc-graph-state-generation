'''
    Example graph state generations
'''

import math
import random
from graph_state_generation.graph_state import graph_state


def graph_no_adjacencies(n_vertices: int):
    '''
        Graph with no adjacencies
    '''
    graph = graph_state.GraphState(n_vertices)
    return graph


def graph_disconnected_bipartied(n_vertices: int):
    '''
        Disconnected bipartied graph
    '''
    graph = graph_state.GraphState(n_vertices)
    for i in range(0, n_vertices - 1, 2):
        graph.append(i, i + 1)

    return graph


def graph_binary_tree(n_vertices: int):
    '''
        Binary tree graph
    '''
    graph = graph_state.GraphState(n_vertices)
    for i in range(n_vertices):
        if i != i // 2:
            graph.append(i, i // 2)
    return graph


def graph_random(n_vertices: int, density=0.1):
    '''
        Random graph
    '''
    graph = graph_state.GraphState(n_vertices)
    for i in range(n_vertices - 1):
        for j in random.sample(
                range(i + 1, n_vertices),
                math.ceil(density * n_vertices - i)):

            graph.append(i, j)

    return graph


def graph_complete(n_vertices: int):
    '''
        Complete graph
    '''
    graph = graph_state.GraphState(n_vertices)
    lst = list(range(n_vertices))
    for i in range(n_vertices):
        graph[i].append(lst[:i], lst[i + 1:])
    return graph


def graph_star(n_vertices: int):
    '''
        Star graph
    '''
    graph = graph_state.GraphState(n_vertices)
    for i in range(1, n_vertices):
        graph.append(0, i)
    return graph
