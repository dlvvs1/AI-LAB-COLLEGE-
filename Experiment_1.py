''' Write a Python program to implement
a) Depth First Search
b) Inheritance
c) Polymorphism'''


# Theory
# a) Depth First Search (DFS):
'''Depth First Search is a graph traversal algorithm that explores as far as possible along
each branch before backtracking. It uses a stack or recursion to traverse nodes. DFS is
widely used in path finding, cycle detection, and topological sorting.'''

# Part A: Depth First Search

'''1. Create a graph using adjacency list.
2. Define a recursive DFS function.
3. Mark visited nodes.
4. Traverse all connected nodes.'''


def dfs(graph, node, visited): 
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]: dfs(graph,neighbour, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
     }
visited = set() 
print("DFS Traversal:") 
dfs(graph, 'A', visited)


# Theory
# b) Inheritance:
'''Inheritance is an Object-Oriented Programming concept where a child class acquires
properties and behaviours (methods) from a parent class. It helps in code reusability,
modularity, and maintainability.'''

# Part B: Inheritance
'''1. Create a base (parent) class.
2. Create a derived (child) class.
3. Access parent class methods using the child class.'''

class Vehicle:
    def display(self):
        print("This is a vehicle")
class Car(Vehicle):
    def show(self):
        print("This is a car")


obj = Car()
obj.display()
obj.show()


# Theory
# c) Polymorphism:
'''Polymorphism means “many forms”. In Python, it allows methods to have the same name
but behave differently based on the object calling them. It improves flexibility and scalability
of programs.'''

# Part C: Polymorphism
'''1. 2. 3. Define a common method name.
Implement different behaviors in different classes.
Call methods using object references.'''

class Dog:
    def sound(self):
        print("Dog barks")
class Cat:
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]
for animal in animals:
    animal.sound()