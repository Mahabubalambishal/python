'''class Stack:
    def __init__(self):
        self.items=[]
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self)==0:
            return "stack is empty"
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def empty(self):
        return len(self)==0
    def size(self):
        return len(self)
stack=Stack()
print(stack)
stack.push(4)
stack.push(5)
print(str(stack))
print(str(stack.pop()))'''



#create stack operation
'''stack=[]
stack.append("mahabub")
stack.append("alam")
stack.append("bishal")
stack.pop()
stack.pop()
stack.pop()
print(str(stack))'''

#stack data stracture  operation
class Stack:
    def __init__(self):
        self.data=[]
    def __len__(self):
        return len(self.data)
    def __str__(self):
        return str(self.data)
    def push(self,item):
        self.data.append(item)
    def pop(self):
        if len(self.data)==0:
            return "stack is empty"
        return self.data.pop()
    def size(self):
        return len(self.data)
    def empty(self):
        return len(self.data)==0
    def firstitem(self):
        if len(self.data):
            return self.data[0]
        return "stack is empty"

    def lastitem(self):
        if len(self.data):
            return self.data[-1]
        return "stack is empty"
stack=Stack()
print(stack)
stack.push("mahabub")
stack.push("alam")
stack.push("bishal")
print(str(stack))
print(stack.pop())
print(stack)
print(stack.size())
print(stack.empty())
print(stack.firstitem())
print(stack.lastitem())


#push and pop operation
'''stack=[]
stack.append("mahabub")
stack.append("alam")
stack.append("bishal")
print(stack)
print(stack.pop())
print(stack)'''
print("hello world!")











