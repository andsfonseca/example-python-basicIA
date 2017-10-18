class Utils:
    def __init__(self):
        pass

    @staticmethod
    def contaisInList(list, obj):
        for item in list:
            if item == obj:
                return True
        return False