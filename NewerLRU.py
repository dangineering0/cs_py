class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class NewerLRU(object):

    def __init__(self, capacity):

        self.capacity = capacity
        self.nodes = {}
        self.head = None
        self.tail = None

    # @return node
    def get(self, key):
        if key not in self.nodes:
            return None
        node = self.nodes[key]

        self.removeAt(node)
        self.appendToHead(node)
        return node

    # @void remove node
    def removeAt(self, node):
        if node is self.head:
            self.head = self.head.next
            if (self.head is not None):
                self.head.prev = None
        elif node is self.tail:
            self.tail.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        del self.nodes[node.key]


    # @void append node to head
    def appendToHead(self, node):
        if self.head is not None:
            node.next = self.head
            self.head.prev = node
        self.head = node
        self.nodes[node.key] = node

    def put(self, key, value):


        if key in self.nodes:
            self.removeAt(self.nodes[key])
            newNode = Node(key, value)
            self.appendToHead(newNode)
        else:
            node = Node(key, value)
            if self.head is None:
                self.head = node
                self.tail = node

            else:
                if (len(self.nodes) == self.capacity):
                    self.removeAt(self.tail)
            self.appendToHead(node)
    def print1(self):
        for k,v in self.nodes.items():
            print(k,v.val)

l = NewerLRU(2)


l.put(0, "val0")


l.put(1, "v1")


l.put(2,"v2")

l.put(2, "v3")

l.print1()

