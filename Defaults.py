from Node import Node
from Utils import Utils
from RiverProblem import RiverProblem

class Defaults:  
    def __init__(self):
        pass
    
    @staticmethod
    def printParams():
        print("cidades", end = "")

    @staticmethod
    def printParamExpectations():
        print("cbucareste", end = "")

    @staticmethod
    def Load(defaultParam, isToPrint = True):
        if not isinstance(defaultParam, str):
            raise ValueError('Impossível ler configuração de um objeto diferente de String')

        defaultParam = defaultParam.lower();

        _mappedNodes = {};

        if defaultParam == "cidades":
            names = {"Arad", "Zerind", "Oradea", "Timisoara",
            "Lugoj", "Mehadia", "Drobeta", "Craiova",
            "Sibiu", "Fagaras", "Rimnicu", "Pitesti",
            "Neamt", "Iasi", "Vaslui", "Bucareste",
            "Giurgiu", "Urziceni", "Hirsova", "Eforie"}

            for name in names:
                _mappedNodes[name] = Node(name)

            _mappedNodes["Arad"].addAdjacencies(_mappedNodes["Sibiu"], 140)
            _mappedNodes["Arad"].addAdjacencies(_mappedNodes["Timisoara"], 118)
            _mappedNodes["Arad"].addAdjacencies(_mappedNodes["Zerind"], 75)
            _mappedNodes["Zerind"].addAdjacencies(_mappedNodes["Oradea"], 71)
            _mappedNodes["Oradea"].addAdjacencies(_mappedNodes["Sibiu"], 151)
            _mappedNodes["Timisoara"].addAdjacencies(_mappedNodes["Lugoj"], 111)
            _mappedNodes["Lugoj"].addAdjacencies(_mappedNodes["Mehadia"], 70)
            _mappedNodes["Mehadia"].addAdjacencies(_mappedNodes["Drobeta"], 75)
            _mappedNodes["Drobeta"].addAdjacencies(_mappedNodes["Craiova"], 120)
            _mappedNodes["Craiova"].addAdjacencies(_mappedNodes["Pitesti"], 138)
            _mappedNodes["Craiova"].addAdjacencies(_mappedNodes["Rimnicu"], 146)
            _mappedNodes["Sibiu"].addAdjacencies(_mappedNodes["Fagaras"], 99)
            _mappedNodes["Sibiu"].addAdjacencies(_mappedNodes["Rimnicu"], 80)
            _mappedNodes["Fagaras"].addAdjacencies(_mappedNodes["Bucareste"], 211)
            _mappedNodes["Rimnicu"].addAdjacencies(_mappedNodes["Pitesti"], 97)
            _mappedNodes["Pitesti"].addAdjacencies(_mappedNodes["Bucareste"], 101)
            _mappedNodes["Neamt"].addAdjacencies(_mappedNodes["Iasi"], 87)
            _mappedNodes["Iasi"].addAdjacencies(_mappedNodes["Vaslui"], 92)
            _mappedNodes["Vaslui"].addAdjacencies(_mappedNodes["Urziceni"], 142)
            _mappedNodes["Bucareste"].addAdjacencies(_mappedNodes["Giurgiu"], 90)
            _mappedNodes["Bucareste"].addAdjacencies(_mappedNodes["Urziceni"], 85)
            _mappedNodes["Urziceni"].addAdjacencies(_mappedNodes["Hirsova"], 98)
            _mappedNodes["Hirsova"].addAdjacencies(_mappedNodes["Eforie"], 86)

            if(isToPrint): print("Configuração de cidades foram carregadas")

        elif (defaultParam == "riverproblem"):
            states = {"btgr|", "tr|bg", "btr|g", "t|bgr", "btg|r",
            "r|btg", "brg|t", "g|btr", "bg|tr", "|btgr" }

            for state in states:
                _mappedNodes[state] = Node(RiverProblem.createStateFromStringParam(state))

            _mappedNodes["btgr|"].addAdjacencies(_mappedNodes["tr|bg"])
            _mappedNodes["tr|bg"].addAdjacencies(_mappedNodes["btr|g"])
            _mappedNodes["btr|g"].addAdjacencies(_mappedNodes["t|bgr"])
            _mappedNodes["btr|g"].addAdjacencies(_mappedNodes["r|btg"])
            _mappedNodes["t|bgr"].addAdjacencies(_mappedNodes["btg|r"])
            _mappedNodes["btg|r"].addAdjacencies(_mappedNodes["g|btr"])
            _mappedNodes["r|btg"].addAdjacencies(_mappedNodes["brg|t"])
            _mappedNodes["brg|t"].addAdjacencies(_mappedNodes["g|btr"])
            _mappedNodes["g|btr"].addAdjacencies(_mappedNodes["bg|tr"])
            _mappedNodes["bg|tr"].addAdjacencies(_mappedNodes["|btgr"])

        else:
            if(isToPrint): print("Nenhuma configuração encontrada")
            return None;

        return _mappedNodes
    
    @staticmethod
    def LoadExpectations(_mappedNodes, expectationTarget):

        if not isinstance(expectationTarget, str):
            raise ValueError('Impossível ler configuração de um objeto diferente de String')

        expectationTarget = expectationTarget.lower();

        _expectations = {}
        if (expectationTarget == "cbucareste"):
            _expectations[_mappedNodes["Arad"]] = 366
            _expectations[_mappedNodes["Bucareste"]] = 0
            _expectations[_mappedNodes["Craiova"]] = 160
            _expectations[_mappedNodes["Drobeta"]] = 242
            _expectations[_mappedNodes["Eforie"]] = 161
            _expectations[_mappedNodes["Fagaras"]] = 176
            _expectations[_mappedNodes["Giurgiu"]] = 77
            _expectations[_mappedNodes["Hirsova"]] = 151
            _expectations[_mappedNodes["Iasi"]] = 226
            _expectations[_mappedNodes["Lugoj"]] = 244
            _expectations[_mappedNodes["Mehadia"]] = 241
            _expectations[_mappedNodes["Neamt"]] = 234
            _expectations[_mappedNodes["Oradea"]] = 380
            _expectations[_mappedNodes["Pitesti"]] = 100
            _expectations[_mappedNodes["Rimnicu"]] = 193
            _expectations[_mappedNodes["Sibiu"]] = 253
            _expectations[_mappedNodes["Timisoara"]] = 329
            _expectations[_mappedNodes["Urziceni"]] = 80
            _expectations[_mappedNodes["Vaslui"]] = 199
            _expectations[_mappedNodes["Zerind"]] = 374
            print("Expectativas até Bucarste foram carregadas")
            return _expectations
        else:
            print("Nenhuma Expectativa encontrada")
            return None;   

                