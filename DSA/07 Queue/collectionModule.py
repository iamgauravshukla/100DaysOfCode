# deque() to create queue
# append() works enqueue as adding elements
# popleft() works as dequeue
# clear()

from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
print(customQueue)
print(customQueue.popleft())
