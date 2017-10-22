from Utils import Utils
class Graph:
    def __init__(self):
        pass

    @staticmethod
    def dictParentToList(dictx, last):
        _return = []
        node = last
        while (not node is None):
            _return.append(node);
            node = dictx[node];
        return _return[::-1]

    @staticmethod
    def BFSearch( final, queue = [] , traveled = [], parent = {}):
        node = None;

        if not isinstance(queue, list):
            node = queue;
            parent[node] = None;
            queue = [];
        else:
            node = queue.pop(0)

        traveled.append(node);

        if(node == final):
            return Graph.dictParentToList(parent, node);
        else:
            for adjacency in node.adjacencies.keys():
                if(not Utils.contaisInList(traveled, adjacency)):
                    queue.append(adjacency)
                    parent[adjacency] = node;
            if(queue):
                return Graph.BFSearch(final, queue, traveled, parent)                
            else:
                return None;

    @staticmethod
    def DjikstraSearch(final, queue = [], traveled = [], parent = {}, euristics = {}):
        node = None;
        euristic = 0;
        if not isinstance(queue, list):
            node = queue;
            parent[node] = None;
            queue = [];
        else:
            node = queue.pop(0)
            euristic = euristics[node]
        traveled.append(node);
        if(node == final):
            return Graph.dictParentToList(parent, node);
        else:
            for adjacency in node.adjacencies.keys():
                if(not Utils.contaisInList(traveled, adjacency)):
                    nextEuristic = euristic + node.adjacencies[adjacency]
                    x = 0;
                    if (queue):
                        for q in queue:
                            if(nextEuristic < euristics[q]):
                                break;
                            x += 1
                    if((Utils.contaisInList(queue, adjacency) and euristics[adjacency] > nextEuristic) or 
                        not Utils.contaisInList(queue, adjacency)):
                        euristics[adjacency] = nextEuristic
                        parent[adjacency] = node;
                    queue.insert(x, adjacency)
            if(queue):
                return Graph.DjikstraSearch(final, queue, traveled, parent, euristics)                
            else:
                return None;

    @staticmethod
    def ASearch(expectations, final, queue = [], traveled = [], parent = {}, euristics = {}, ):
        node = None;
        euristic = 0;
        if not isinstance(queue, list):
            node = queue;
            parent[node] = None;
            queue = [];
        else:
            node = queue.pop(0)
            euristic = euristics[node]
        traveled.append(node);
        if(node == final):
            return Graph.dictParentToList(parent, node);
        else:
            for adjacency in node.adjacencies.keys():
                if(not Utils.contaisInList(traveled, adjacency)):
                    nextEuristic = euristic + node.adjacencies[adjacency] 
                    x = 0;
                    if (queue):
                        for q in queue:
                            if(nextEuristic + expectations[adjacency] < euristics[q]):
                                break;
                            x += 1
                    if((Utils.contaisInList(queue, adjacency) and euristics[adjacency] > nextEuristic) or 
                        not Utils.contaisInList(queue, adjacency)):
                        euristics[adjacency] = nextEuristic
                        parent[adjacency] = node;
                    queue.insert(x, adjacency)
            if(queue):
                for q in queue:
                    print(expectations[q], end=" ")
                    print()
                return Graph.DjikstraSearch(final, queue, traveled, parent, euristics)                
            else:
                return None;