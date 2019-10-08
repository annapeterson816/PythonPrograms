class Circle():
   
   def __init__(self, radius):
      if type(radius)!=int and type(radius)!=float:
         raise TypeError

      if radius < 0:
         raise ValueError

      #if you do double underscore, it is now PRIVATE
      self.__radius=radius

   def __str__(self):
      return "Radius of the circle is: " + str(self.__radius)

   def setRadius(self,radius):
      if type(radius)!=int and type(radius)!=float:
         raise TypeError

      if radius < 0:
         raise ValueError
      self.__radius=radius

   def __add__(self, another_circle):
      return Circle(self.__radius + another_circle.__radius)
      

   


C1= Circle(4)
print C1
#C2= Cricle("9") #raise an error
#C3= Circle(-3) #raise an error
C1.setRadius(99)
C4=Circle(1)
C5= C4 + C1
print C5
