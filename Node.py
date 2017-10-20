
class Node:
    def __init__(self, name):
        self.name = name
        self.adjacencies = {}

    def addAdjacencies(self, node, distance):
        if(self.searchAdjacencies(node) is None):
            self.adjacencies[node] = distance
            node.addAdjacencies(self, distance)

    def searchAdjacencies(self, node):
        for adjacency in self.adjacencies.keys(): 
            if adjacency == node:
               return self.adjacencies[node];
        return None

    def printNode(self, short = False):
        if(short):  print(self.name, end="")
        else:
            print("Nome do Node: ", self.name)
            print("Adjacências: ")
            for adjacency in self.adjacencies.keys(): 
                print("    ", adjacency.name, ": ", self.adjacencies[adjacency])
            print()

