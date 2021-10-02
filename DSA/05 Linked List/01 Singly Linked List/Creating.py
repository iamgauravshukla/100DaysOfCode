
class SinglyLinked:
    def __init__(self):
        self.head = None
        self.tail = None
class Nodes:
    def __init__(self, value=None):
        self.value = value
        self.next = None

SinglyLinkedList = SinglyLinked()

node1 = Nodes(1)
node2 = Nodes(2)

SinglyLinkedList.head = node1
SinglyLinkedList.head.next = node2
SinglyLinkedList.tail = node2

