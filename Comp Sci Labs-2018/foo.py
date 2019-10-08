class foo:
   def __init__(self, x):
      self.x=x
      
   def __less__(self, other):
      if self.x<other.x:
         return True
      else:
         return False

f=foo()
format(foo)
a =f(2)
b= f(3)
print (a<b)
