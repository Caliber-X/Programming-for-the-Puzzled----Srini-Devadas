# Programming for the Puzzled -- Srini Devadas
# A Weekend to Remember
# By Caliber_X


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

# disconnected graphs
dgraph = { 'B': ['C'],
           'C': ['B', 'D'],
           'D': ['C', 'E', 'F'],
           'E': ['D'],
           'F': ['D', 'G', 'H', 'I'],
           'G': ['F'],
           'H': ['F'],
           'I': ['F'],
          'F1': ['D1', 'I1', 'G1', 'H1'],
          'B1': ['C1'],
          'D1': ['C1', 'E1', 'F1'],
          'E1': ['D1'],
          'H1': ['F1'],
          'C1': ['D1', 'B1'],
          'G1': ['F1'],
          'I1': ['F1']}

dgraph2 = {'F': ['D', 'I', 'G', 'H'],
           'B': ['C'],
           'D': ['C', 'E', 'F'],
           'E': ['D'],
           'H': ['F'],
           'C': ['D', 'B'],
           'G': ['F'],
           'I': ['F'],
           'A1': ['B1', 'C1'],
           'B1': ['A1', 'C1'],
           'C1': ['A1', 'B1']}

dgraph3 = {'A': ['B'],
           'B': ['A'],
           'C': ['D'],
           'D': ['C', 'E', 'F'],
           'E': ['D'],
           'F': ['D', 'G', 'H', 'I'],
           'G': ['F'],
           'H': ['F'],
           'I': ['F']}

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

def colorGraph(graph):
    coloring = {}
    for node in graph:  # if disconnected graph -> iterate through all nodes
        if node in coloring:
            continue
        val, coloring = bipartiteGraphColor(graph, node, coloring, color=0)
        if not val:
            return False, {}
    return True, coloring

# denoting color using binary = bipartite

# print (bipartiteGraphColor(gra3, 'A', {}, 0))
# print (bipartiteGraphColor(graph, 'B', {}, 0))
# print (bipartiteGraphColor(graph2, 'F', {}, 0))
# print (bipartiteGraphColor(grap, 'A', {}, 0))

print (colorGraph(gra3))
print (colorGraph(graph))
print (colorGraph(graph2))
print (colorGraph(grap))

print(colorGraph(dgraph))
print(colorGraph(dgraph2))
print(colorGraph(dgraph3))
