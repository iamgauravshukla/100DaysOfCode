class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        if self.LinkedList.head == None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.isEmpty():
            return 'There is not any element'
        else:
            nodeValue = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return nodeValue

    def peak(self):
        if self.isEmpty():
            return 'There is not any element'
        else:
            nodeValue = self.LinkedList.head.value
            return nodeValue

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(5)
customStack.push(9)
customStack.push(10)
print(customStack)
print("*****")
customStack.pop()
print(customStack.peak())
print(customStack.isEmpty())