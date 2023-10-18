
adjacency_table = { 
    'A': ['B', 'C'], 
    'B': ['A', 'C'], 
    'C': ['A', 'B', 'D'], 
    'D': ['C', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E'] 
    }

# def find_neighbors(adjacency_table, vertex):
#     return adjacency_table[vertex]

def is_neighbor(adjacency_table, vertex1, vertex2):
    if vertex2 in adjacency_table[vertex1]:
        return True
    else:
        return False

adjacency_table = { 
    'A': ['B', 'C'], 
    'B': ['A', 'C'], 
    'C': ['A', 'B', 'D'], 
    'D': ['C', 'E', 'F'],
    'E': ['D', 'F'],
    'F': ['D', 'E'] 
    } # Add your code here

def find_neighbors(vertex, adjaceny_table):
    # Add your code here
    return adjacency_table[vertex]

def is_neighbor(vertex1, vertex2, adjacency_table):
    # Add your code here
    if vertex2 in adjacency_table[vertex1]:
        return True
    else:
        return False

print(find_neighbors('A', adjacency_table)) # should print ['B', 'C']
print(find_neighbors('D', adjacency_table)) # should print ['C', 'E', 'F']

print(is_neighbor('A','B',adjacency_table)) # True
print(is_neighbor('D','F',adjacency_table)) # True
print(is_neighbor('C','F',adjacency_table)) # False