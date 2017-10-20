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
    def DjikstraSearch(final, queue = [], traveled = [], parent = {}, expectation = []):
        node = None;

        if not isinstance(queue, list):
            node = queue;
            parent[node] = None;
            queue = [];
        else:
            node = queue.pop(0)
            expectation.pop(0)

        traveled.append(node);

        if(node == final):
            return Graph.dictParentToList(parent, node);
        else:
            for adjacency in node.adjacencies.keys():
                if(not Utils.contaisInList(traveled, adjacency)):
                    x = 0;
                    if (queue):
                        for q in queue:
                            if(expectation[x] > node.adjacencies[adjacency]):
                                break
                            x += 1
                    queue.insert(x, adjacency)
                    expectation.insert(x, node.adjacencies[adjacency])    

                    parent[adjacency] = node;
            print("===============")
            for q in queue:
                q.printNode()
            input()
            if(queue):
                return Graph.DjikstraSearch(final, queue, traveled, parent, expectation)                
            else:
                return None;
