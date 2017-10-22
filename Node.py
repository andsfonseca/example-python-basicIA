class Node:
    def __init__(self, value):
        self.value = value
        self.adjacencies = {}

    def addAdjacencies(self, node, distance = 0):
        if(self.searchAdjacencies(node) is None):
            self.adjacencies[node] = distance
            node.addAdjacencies(self, distance)

    def searchAdjacencies(self, node):
        for adjacency in self.adjacencies.keys(): 
            if adjacency == node:
               return self.adjacencies[node];
        return None

    def printNode(self, short = False):
        if(short):  print(self.value, end="")
        else:
            print("Valor do Node: ", self.value)
            print("Adjacências: ")
            for adjacency in self.adjacencies.keys(): 
                print("    ", adjacency.value, ": ", self.adjacencies[adjacency])
            print()

