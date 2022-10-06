class Queue:
    def __init__(self):
        self.items = []
    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of Queue"

    def dequeue(self):
        if not self.items:
            return 'empty queue'
        else:
            return self.items.pop(0)

    def peek(self):
        if self.items == []:
            return 'empty queue'
        else:
            return self.items[0]

    def delete(self):
        self.items = None



customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(4)
customQueue.enqueue(3)
customQueue.enqueue(1)
customQueue.dequeue()
print(customQueue)