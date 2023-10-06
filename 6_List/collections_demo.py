from collections import deque

queue = deque(["Eric", "John", "Michael"])  # create a list
queue.append("Terry")  # Terry arrives
queue.append("Graham")  # Graham arrives
person = queue.popleft()  # The first to arrive now leaves
print(person)
print(queue)
queue.popleft()                 # The second to arrive now leaves
print(queue)