# Queues follow the First In First Out (FIFO) principle.

from collections import deque   

# Creating a queue

queue = deque()

# Enqueueing elements

queue.append(1)
queue.append(3)
queue.append(5)
queue.append(7)
queue.append(9)

print(queue)

# Dequeueing elements
print(queue.popleft())

print(queue)
