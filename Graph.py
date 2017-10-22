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
    def DjikstraSearch(final, queue = [], traveled = [], parent = {}, expectation = {}):
        node = None;
        euristic = 0;

        if not isinstance(queue, list):
            node = queue;
            parent[node] = None;
            queue = [];
        else:
            node = queue.pop(0)
            euristic = expectation[node]

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
                            if(nextEuristic < expectation[q]):
                                break;
                            x += 1

                    if((Utils.contaisInList(queue, adjacency) and expectation[adjacency] > nextEuristic) or 
                        not Utils.contaisInList(queue, adjacency)):
                        expectation[adjacency] = nextEuristic
                        parent[adjacency] = node;
                    queue.insert(x, adjacency)
            if(queue):
                return Graph.DjikstraSearch(final, queue, traveled, parent, expectation)                
            else:
                return None;