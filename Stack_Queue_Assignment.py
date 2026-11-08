class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"
        
    def peek (self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"
        
    def size(self):
        return len(self.items)
    
    def display(self):
        return self.items
    
myStack = Stack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.push(6)
myStack.push(7)
myStack.push(8)
myStack.push(9)
myStack.push(10)

print("Stack: ")
print(myStack.display())

class Queue:
    from queue import Queue
    q = Queue(maxsize = 10)
    q.put('1')
    q.put('2')
    q.put('3')
    q.put('4')
    q.put('5')
    q.put('6')
    q.put('7')
    q.put('8')
    q.put('9')
    q.put('10')
    
    print("\nQueue: ")
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())


