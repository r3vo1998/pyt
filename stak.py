<<<<<<< HEAD
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
s = ["1", "2", "3", "4", "5"]
for c in s:
    stack.push(c)

    
reverse = ""
for i in range(len(stack.items)):
    reverse += stack.pop()
=======
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        last = len(self.items)-1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
s = ["1", "2", "3", "4", "5"]
for c in s:
    stack.push(c)

    
reverse = ""
for i in range(len(stack.items)):
    reverse += stack.pop()
>>>>>>> ac5d2c7ba8c62d0e5ba2b0895e95f3b71ed59ce6
