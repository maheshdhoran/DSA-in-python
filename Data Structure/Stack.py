#Implementing Stack using deque
#complexity of code O(1)

from collections import deque

stack=deque()

stack.append(1)
stack.append(2)
stack.append(3)
print("Initial Stack")
print(stack)

stack.pop()
stack.pop()
print("Stack after removing 2 elements")
print(stack)

stack.pop()
print("Empty Stack")
print(stack)