# Programming for the Puzzled -- Srini Devadas
# A Weekend to Remember
# By Caliber_X


def bipartiteGraphColor(graph, start, coloring, color):

    if start not in graph:  # not a graph / undirected graph
        return False, {}

    # base case - already colored
    if start in coloring:
        # if already colored - check color
        if coloring[start] != color:    # color mismatch
            return False, coloring
        return True, coloring

    coloring[start] = color
    for node in graph[start]:
        # print(f"{start, node} -> {coloring}")
        val, coloring = bipartiteGraphColor(graph, node, coloring, 1 - color)
        if not val:
            return False, {}

    return True, coloring


graph = {'B': ['C'],
         'C': ['B', 'D'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'F': ['D', 'G', 'H', 'I'],
         'G': ['F'],
         'H': ['F'],
         'I': ['F']}

graph2 = {'F': ['D', 'I', 'G', 'H'],
         'B': ['C'],
         'D': ['C', 'E', 'F'],
         'E': ['D'],
         'H': ['F'],
         'C': ['D', 'B'],
         'G': ['F'],
         'I': ['F']}

gra3 = {'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']}

grap = {'A': ['B', 'D'],
        'B': ['C', 'A'],
        'C': ['D', 'B'],
        'D': ['A', 'C']}

# denote color using binary = bipartite
print (bipartiteGraphColor(gra3, 'A', {}, 0))
print (bipartiteGraphColor(graph, 'B', {}, 0))
print (bipartiteGraphColor(graph2, 'F', {}, 0))
print (bipartiteGraphColor(grap, 'A', {}, 0))
