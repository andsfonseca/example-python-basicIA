from Graph import Graph
from Utils import Utils

class NumberPuzzle:
    
    _bestCondition = [[0,1,2],[3,4,5],[6,7,8]]

    @staticmethod
    def getExpectationToNumberPuzzle(stateNumberPuzzle):
        _expectation = 0
        x = 0;
        for line in stateNumberPuzzle:
            y = 0;
            for number in line:
                idealLine, idealColumn = NumberPuzzle.getIdealPosition(number)
                _expectation += (abs( x - idealLine) + abs(y - idealColumn))
                ###print(idealLine, idealColumn, number, _expectation)
                y += 1
            x += 1
        ###print(_expectation)
        return _expectation

    @staticmethod
    def getIdealPosition(n):
        x = 0;
        for line in NumberPuzzle._bestCondition:
            y = 0;
            for number in line:
                if(number == n):
                    return x, y;
                y += 1
            x += 1

    @staticmethod
    def getPossibilities(stateNumberPuzzle):

        maxLen = len(stateNumberPuzzle) - 1
        possibilities = []
        x = 0;
        found = False;
        for line in stateNumberPuzzle:
            y = 0;
            for number in line:
                if(number == 0):
                    if(not x == 0):
                        newState = NumberPuzzle.copyPuzzle(stateNumberPuzzle)
                        newState[x][y], newState[x-1][y] = newState[x-1][y], newState[x][y]
                        possibilities.append(newState)
                    if(not x == maxLen):
                        newState = NumberPuzzle.copyPuzzle(stateNumberPuzzle)
                        newState[x][y], newState[x+1][y] = newState[x+1][y], newState[x][y]
                        possibilities.append(newState)
                    if(not y == 0):
                        newState = NumberPuzzle.copyPuzzle(stateNumberPuzzle)
                        newState[x][y], newState[x][y-1] = newState[x][y-1], newState[x][y]
                        possibilities.append(newState)
                    if(not y == maxLen):
                        newState = NumberPuzzle.copyPuzzle(stateNumberPuzzle)
                        newState[x][y], newState[x][y+1] = newState[x][y+1], newState[x][y]
                        possibilities.append(newState)
                    found = True;
                if(found): break;
                y += 1
            if(found): break;
            x += 1

        return possibilities

    @staticmethod
    def copyPuzzle(stateNumberPuzzle):
        '''Copia o Puzzle'''
        _return = []
        copyLine = [] 
        for line in stateNumberPuzzle:
            copyLine = [] 
            for number in line:
                '''Multiplicar por 1 para retornar o valor em vez de uma referência'''
                copyLine.append(int(number/1))
            _return.append(copyLine)
        return _return

    @staticmethod
    def hashPuzzzle(stateNumberPuzzle):
        '''Transforma em um padrão em String'''
        _string = ""
        i = 0
        for line in stateNumberPuzzle:
            for number in line:
                _string += str(number)
                _string += "|" if not i == 8 else ""
                i += 1
        return _string

    @staticmethod
    def deHashPuzzzle(string):
        '''Transforma uma string bruta em um node'''
        s = string.split("|")
        return [[int(s[0]), int(s[1]), int(s[2])],
        [int(s[3]), int(s[4]), int(s[5])],
        [int(s[6]), int(s[7]), int(s[8])]]


    @staticmethod
    def ASearch(queue = [], firstExecution = True, traveled = [], parent = {}, euristics = {}):
        node = None;
        euristic = 0;

        if firstExecution:
            node = queue;
            parent[NumberPuzzle.hashPuzzzle(node)] = None;
            queue = [];
        else:
            for q in queue: 
                print(q, euristics[q], NumberPuzzle.getExpectationToNumberPuzzle(NumberPuzzle.deHashPuzzzle(q)))

            
            node = NumberPuzzle.deHashPuzzzle(queue.pop(0))
            euristic = euristics[NumberPuzzle.hashPuzzzle(node)]

        traveled.append(NumberPuzzle.hashPuzzzle(node));

        if(node == NumberPuzzle._bestCondition):
            return Graph.dictParentToList(parent, NumberPuzzle.hashPuzzzle(node));
        else:
            for adjacency in NumberPuzzle.getPossibilities(node):
                if(not Utils.contaisInList(traveled, NumberPuzzle.hashPuzzzle(adjacency))):
                    nextEuristic = euristic + 1 + NumberPuzzle.getExpectationToNumberPuzzle(adjacency)## O custo de se mover é apenas 1
                    x = 0;
                    if (queue):
                        for q in queue:
                            if(nextEuristic < euristics[q]):
                                break;
                            x += 1

                    if((Utils.contaisInList(queue, NumberPuzzle.hashPuzzzle(adjacency)) and euristics[NumberPuzzle.hashPuzzzle(adjacency)] > nextEuristic) or 
                        not Utils.contaisInList(queue, NumberPuzzle.hashPuzzzle(adjacency))):
                        euristics[NumberPuzzle.hashPuzzzle(adjacency)] = nextEuristic
                        parent[NumberPuzzle.hashPuzzzle(adjacency)] = NumberPuzzle.hashPuzzzle(node);
                    queue.insert(x, NumberPuzzle.hashPuzzzle(adjacency))
            if(queue):
                '''
                for q in queue: 
                    print(q, euristics[q], NumberPuzzle.getExpectationToNumberPuzzle(NumberPuzzle.deHashPuzzzle(q)))

                input()
                '''
                return NumberPuzzle.ASearch(queue, False, traveled, parent, euristics)                
            else:
                return None;
        
        



    
        

