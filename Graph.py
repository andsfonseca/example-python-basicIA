from Utils import Utils
class Search:
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
    def BreadthFirst( final, queue = [] , traveled = [], parent = {}):

        node = None;

        if not isinstance(queue, list):
            node = queue;
            parent[node] = None;
            queue = [];
        else:
            node = queue.pop(0)

        traveled.append(node);

        if(node == final):
            return Search().dictParentToList(parent, node);
        else:
            for adjacency in node.adjacencies.keys():
                if(not Utils.contaisInList(traveled, adjacency)):
                    queue.append(adjacency)
                    parent[adjacency] = node;
            if(queue):
                return Search().BreadthFirst(final, queue, traveled, parent)                
            else:
                return None;
