class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in self.list]
        return '\n'.join(values)

    # Stack operations
    # isEmpty
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

    # Push
    def push(self, value):
        self.list.append(value)
        print('Element Successfully pushed into stack')

    #Pop
    def pop(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list.pop()

    # Peak
    def peak(self):
        if self.isEmpty():
            return 'The stack is empty'
        else:
            return self.list[len(self.list) - 1]

    #delete
    def delete(self):
        self.list = None




customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)

print(customStack.pop())

