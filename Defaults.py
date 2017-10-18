from Node import Node
class Defaults:  
    def __init__(self):
        pass
    
    @staticmethod
    def Load(defaultParam):
        if not isinstance(defaultParam, str):
            raise ValueError('Impossível ler configuração de um objeto diferente de String')

        _mappedNodes = {};

        if defaultParam == "Cidades":
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
        else:
            print("Nenhuma configuração encontrada")

        return _mappedNodes
            