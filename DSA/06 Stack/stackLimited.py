class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    #isFull
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            False

    #Push
    def push(self, value):
        if self.isFull():
            return  'The Stack is Full'
        else:
            self.list.append(value)

    # Pop
    def pop(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            return self.list.pop()

    #Peak
    def peak(self):
        if self.isEmpty():
            return 'Stack is Empty'
        else:
            return self.list[len(self.list) - 1]

    #delete
    def delete(self):
        self.list = None



customStack = Stack(10)
print(customStack.isEmpty())
print(customStack.isFull())
customStack.push(3)
customStack.push(9)
print(customStack)

print(customStack.pop())

