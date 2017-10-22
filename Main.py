'''Imports'''
from Node import Node
from Defaults import Defaults
from Graph import Graph

import sys
import os

sys.setrecursionlimit(3000)   

def showNodesList(nodesList):
    for nodeKey in nodesList:
        nodeKey.printNode(True);
        if(nodesList[len(nodesList) - 1] == nodeKey): print(" ", end="")
        else: print(" ", end=" -> ")
    print()

def main():
    m_mappednodes = None
    option = 0
    while True:
        os.system('cls')
        if(option == 0):
            print('{:=^15}'.format(' Menu '))
            print("1 -> Carregar Predefinições")
            print("2 -> Mostrar Nodes Mapeados")
            print("3 -> Realizar Busca")
            print("4 -> Sair")
            option = int(input("Opção Selecionada: "))
        elif (option == 1):
            print("Escolha uma predefição: ")
            print("Predefinições Disponíves = ", end="{")
            Defaults.printParams()
            print("}")
            print()
            predefName = input("Predefição Selecionada: ")
            m_mappednodes = Defaults.Load(predefName)
            input("Pressione Enter para Continuar")
            option = 0
        elif (option == 2):
            if(m_mappednodes is None):
                print("Nenhum Node Mapeado")
            else:
                for nodeKey in m_mappednodes.keys():
                    m_mappednodes[nodeKey].printNode()
            input("Pressione Enter para Continuar")
            option = 0;
        elif (option == 3):
            if(m_mappednodes is None):
                print("Nenhum Node Mapeado")
            else:
                print("Escolha uma algoritmo: ")
                print("1 -> BreadthFirst")
                print("2 -> Djikstra")
                print("3 -> A*")
                print()
                suboption = int(input("Algoritmo Selecionado: "))
                nodeKeyStart = input("Ponto de Partida: ")
                nodeKeyFinal = input("Ponto de Chegada: ")
                print()
                if(suboption == 1):
                    showNodesList(Graph.BFSearch(m_mappednodes[nodeKeyFinal], m_mappednodes[nodeKeyStart]))
                elif(suboption == 2):
                    showNodesList(Graph.DjikstraSearch(m_mappednodes[nodeKeyFinal], m_mappednodes[nodeKeyStart]))
                elif(suboption == 3):
                    print("Escolha uma Expectativa")
                    print("Expectativas Disponíves = ", end="{")
                    Defaults.printParamExpectations()
                    print("}")
                    print()
                    predefName = input("Expectativa Selecionada: ")
                    expectations = Defaults.LoadExpectations(m_mappednodes, predefName)
                    if(not expectations is None):
                        showNodesList(Graph.ASearch(expectations, m_mappednodes[nodeKeyFinal], m_mappednodes[nodeKeyStart]))
            input("Pressione Enter para Continuar")
            option = 0
        elif (option == 4):
            break
        else:
            print("Este não é um comando válido")
            input("Pressione Enter para Continuar")
            option = 0;

main();

