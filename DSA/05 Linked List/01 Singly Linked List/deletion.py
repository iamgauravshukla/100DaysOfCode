class Nodes:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinked:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List
    def insertSL(self, value, location):
        newNode = Nodes(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    # Traversal
    def traversal(self):
        if self.head is None:
            print('Single linked list does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    #Deletion
    def delNode(self, location):
        if self.head is None:
            print("The singly linked list doesn't exist")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


SinglyLinkedList = SinglyLinked()
SinglyLinkedList.insertSL(1, 1)
SinglyLinkedList.insertSL(2, 1)
SinglyLinkedList.insertSL(3, 0)
SinglyLinkedList.insertSL(4, 2)

print([node.value for node in SinglyLinkedList])
SinglyLinkedList.delNode(0 )
print([node.value for node in SinglyLinkedList])



