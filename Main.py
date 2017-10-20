'''Imports'''
from Node import Node
from Defaults import Defaults
from Graph import Graph
import sys
sys.setrecursionlimit(3000) 
def showMappedNodes():
    for nodeKey in m_mappednodes.keys():
        m_mappednodes[nodeKey].printNode()

def showNodesList(nodesList):
    for nodeKey in nodesList:
        nodeKey.printNode(True);
        if(nodesList[len(nodesList) - 1] == nodeKey): print(" ", end="")
        else: print(" ", end=" -> ")
    print()

m_mappednodes = Defaults.Load("Cidades")
##showMappedNodes();
bfsResult = Graph.DjikstraSearch(m_mappednodes["Bucareste"], m_mappednodes["Arad"])
showNodesList(bfsResult)
