"""This files defines functions dealing with dominated vertices. A
vertex :math:`v` in a graph :math:`G` is a vertex such that there is
another vertex :math:`w` that..

"""
import copy


def closed_neighborhood(g, v):
    return set(g[v]) | {v}


def is_dominated_vertex(g, v):
    for u in g:
        if u != v:
            if closed_neighborhood(g, v).issubset(closed_neighborhood(g, u)):
                return True
    else:
        return False


def has_dominated_vertex(g):
    for v in g:
        if is_dominated_vertex(g, v):
            return [v]
    else:
        return False


def remove_dominated_vertex(g):
    g1 = copy.deepcopy(g)
    x = has_dominated_vertex(g)
    if not x:
        return g1
    else:
        g1.remove_node(x[0])
        return g1


def completely_pared_graph(g):
    g1 = copy.deepcopy(g)
    while True:
        n = g1.order()
        g1 = remove_dominated_vertex(g1)
        if n == g1.order():
            return g1
