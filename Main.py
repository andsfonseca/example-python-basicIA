'''Imports'''
from Defaults import Defaults
from Graph import Graph

from NumberPuzzle import NumberPuzzle

import sys
import os

##Argumento para limpar tela de acordo com o sistema
_clearargument = "cls" if os.name == "nt" else "clear" 

##Os algoritmos usam recursão, está função permite que eu permita chamar mais algumas funções dentro de uma recursividade
sys.setrecursionlimit(3000)   

def showNodesList(nodesList):
    '''Imprime uma lista de nós uma linha'''
    for nodeKey in nodesList:
        nodeKey.printNode(True);
        if(nodesList[len(nodesList) - 1] == nodeKey): print(" ", end="")
        else: print(" ", end=" -> ")
    print()

def main():

    m_mappednodes = None
    option = 0

    while True:
        os.system(_clearargument)

        if(option == 0):
            print('{:=^15}'.format(' Menu '))
            print("1 -> Aloritmos de Busca")
            print("2 -> Problema do Rio")
            print("3 -> Quebra Cabeça")
            print("4 -> Sair")
            option = int(input("Opção Selecionada: "))

        elif (option == 1):
            '''Esta opção carrega as cidades e pede a execução de um algoritmo'''
            m_mappednodes = Defaults.Load("cidades")
            
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
                    '''BFS'''
                    showNodesList(Graph.BFSearch(m_mappednodes[nodeKeyFinal], m_mappednodes[nodeKeyStart]))
                elif(suboption == 2):
                    '''Djikstra'''
                    showNodesList(Graph.DjikstraSearch(m_mappednodes[nodeKeyFinal], m_mappednodes[nodeKeyStart]))
                elif(suboption == 3):
                    '''A* (As única expectativa existe é até Bucareste'''
                    expectations = Defaults.LoadExpectations(m_mappednodes, "cbucareste")
                    if(not expectations is None):
                        showNodesList(Graph.ASearch(expectations, m_mappednodes[nodeKeyFinal], m_mappednodes[nodeKeyStart]))

            input("Pressione Enter para Continuar")
            option = 0

        elif (option == 2):
            '''Esta opção carrega os estados do Rio e Imprime os Estados'''
            _riverMappedNotes = Defaults.Load("RiverProblem")
            result = Graph.BFSearch(_riverMappedNotes["|btgr"], _riverMappedNotes["btgr|"])

            count = 0
            for r in result:
                count +=1
                print("Estado ", count, ": ")
                r.value.print()
                print()

            input("Pressione Enter para Continuar")
            option = 0

        elif (option == 3 ):

            puzzle = [[7,2,4],[5, 0, 6], [8,3,1]]
            '''
            puzzle = [[int(input("[Elemento 1]: ")),
                    int(input("[Elemento 2]: ")),
                    int(input("[Elemento 3]: "))],
                    [int(input("[Elemento 4]: ")),
                    int(input("[Elemento 5]: ")),
                    int(input("[Elemento 6]: "))],
                    [int(input("[Elemento 7]: ")),
                    int(input("[Elemento 8]: ")),
                    int(input("[Elemento 9]: "))]]
            '''
            possibilities = NumberPuzzle.getPossibilities(puzzle)
            result = NumberPuzzle.ASearch(puzzle)
            for r in result:
                print(r);
            
            input("Pressione Enter para Continuar")
            option = 0;
        elif (option == 4):
            '''Esta opção sai do While'''
            break
        else:
            '''Esta opção é apenas quando um comando inválido não foi inserico corretamente'''
            print("Este não é um comando válido")
            input("Pressione Enter para Continuar")
            option = 0;

main();

