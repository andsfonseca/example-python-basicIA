class RiverProblemState:

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def print(self):
        
        print("Esquerdo: ", end="")
        for l in self.left:
            if(self.left[len(self.left) - 1] == l): print(l, end="")
            else: print(l, end=", ")
        print()
        print('{:~^40}'.format('-'))
        print('{:~^40}'.format('-'))
        print("Direito: ", end="")
        for r in self.right:
            if(self.right[len(self.right) - 1] == r): print(r, end="")
            else: print(r, end=", ")
        
        print()

class RiverProblem:

    @staticmethod
    def createStateFromStringParam(stringParam):
        count = 0
        left = []
        right = []
        current = ""
        while (not current == '|'):
            current = stringParam[count]
            if(current == 'b') : left.append("Barqueiro")
            elif(current == 't') : left.append("Trigo")
            elif(current == 'g') : left.append("Galinha")
            elif(current == 'r') : left.append("Raposa")
            count += 1
        while (count < len(stringParam)):
            current = stringParam[count]
            if(current == 'b') : right.append("Barqueiro")
            elif(current == 't') : right.append("Trigo")
            elif(current == 'g') : right.append("Galinha")
            elif(current == 'r') : right.append("Raposa")
            count += 1
            
        river = RiverProblemState(left, right)
        
        return river
        