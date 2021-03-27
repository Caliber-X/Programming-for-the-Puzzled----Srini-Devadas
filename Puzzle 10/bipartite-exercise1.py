#Programming for the Puzzled -- Srini Devadas
#A Weekend to Remember
#This puzzle deals with the problem of inviting friends to dinner over two days
#such that no two of your friends who dislike each other are invited on the same
#day.  This can be done if the graph is a bipartite graph.

#The code determines if a graph is bipartite or not. If the graph can be colored
#using two colors, it is bipartite, else it is not.

#Exercise 1: The code shown in the book assumes that all vertexs are reachable
#from the start vertex. Write a procedure that determines whether a possibly
#disconnected graph is bipartite or not.

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
    if start not in graph:
        return False, {}
    
    if start not in coloring:
        coloring[start] = color
    elif coloring[start] != color:
        return False, {}
    else:
        return True, coloring
    
    if color == 'Sha':
        newcolor = 'Hat'
    else:
        newcolor = 'Sha'
        
    for vertex in graph[start]:
        val, coloring = bipartiteGraphColor(graph, vertex, coloring, newcolor)
        if val == False:
            return False, {}
        
    return True, coloring


#Color every vertex in the possibly disconnected graph
def colorDisconnectedGraph(graph, coloring):
    for g in graph:
        if g not in coloring:
            success, coloring = bipartiteGraphColor(graph, g, coloring, 'Sha')
            if not success:
                return False, {}
            
    return True, coloring
        
print (colorDisconnectedGraph(dgraph, {}))
print (colorDisconnectedGraph(dgraph2, {}))
print (colorDisconnectedGraph(dgraph3, {}))
