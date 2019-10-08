class Stack:
   def __init__(self):
      self.items=[]

   def isEmpty(self):
      return (self.items == [])

   def push(self, item): #adds an item to the top of the stack
      self.items.append(item)

   def pop(self):
      return self.items.pop()

   def peek(self):
      return self.items[len(sef.items)-1]

   def size(self):
      return len(self.items)

   def __str__(self):
      return "Elements in the stack are: " + str(self.items)
   
   

s= Stack()
s.push(4)
s.push(10)
s.push(18)
s.push(21)

print s

