class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.parent = None
        self.child = None

    def setParent(self, parent):
        self.parent = parent

    def setChild(self, child):
        self.child = child


class LRUCache(object):
    def __init__(self, capacity):
        self.size = capacity
        self.nodes = {}
        self.head = None
        self.tail = None

    def set(self, key, val):

        node = Node(key, val)  # (1, "val1

        if self.head is None:
            self.head = node

        if self.tail is None:
            self.tail = node

        # check capacity
        self.curSize = len(self.nodes)
        if self.curSize == self.size:
            self.removeLast()

        if node not in self.nodes:
            self.nodes[key] = node
        else:
            self.nodes[key].val = val
            self.removeAt(node)

        self.appendHead(node)

    # get does not remove a item from nodes key

    def get(self, key):
        if key not in self.nodes:
            return None

        node = self.nodes[key]

        self.appendHead(node)

        self.removeAt(node)

        return node

    def appendHead(self, node):
        self.head.setParent(node)
        node.setChild(self.head)
        self.head = self.head.parent

    def removeAt(self, node):

        if node not in self.nodes:
            return

        if node is self.head:
            self.head = self.head.child
            node.child.parent = node.parent
            return

        if node is self.tail:
            self.tail = self.tail.parent
            self.tail.child = None
            return

        node.child.parent = node.parent
        node.parent.child = node.child

        # self.nodes.pop(node.key, None)

