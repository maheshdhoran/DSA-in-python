#Implementing Queue using deque
#complexity of code O(1)

from collections import deque

queue=deque()

queue.append(1)
queue.append(2)
queue.append(3)
print("Initial Queue")
print(queue)

queue.popleft()
queue.popleft()
print("Queue after removing 2 elements")
print(queue)

queue.popleft()
print("Empty Queue")
print(queue)