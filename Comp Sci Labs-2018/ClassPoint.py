import math
from Tkinter import*
master = Tk()
w = Canvas(master, width=1000, height=1000)

class Point():

   #Global members for class Point
   counter=0
   
   #Function members
   def __init__(self, x_coord, y_coord, n_name):
      self.x= x_coord
      self.y= y_coord
      self.name=n_name
      Point.counter=Point.counter+1
   

   #what you would do if you didnt have __str__, not as effective/easy
   def print_Point(self):
      print "Coordinates of", self.name ,"are:", self.x, self.y

   #like a toString, best way
   def __str__ (self):
      return self.name + ": ("+ str(self.x) + "," + str(self.y) + ")"

   def setX(self,x):
      if type(x)== int:
         self.x=x

   def setY(self,y):
      if type(y)==int:
         self.y=y

   def getX(self):
      return self.x
   
   def getY(self):
      return self.y

   #P1=self, P2=other
   def distance(self, other):
      result= math.sqrt((other.x-self.x)**2 + (other.x-self.y)**2)
      return result

   def triangle(self, other, other2):
      line1= w.create_line(self.x*10,self.y*10, other.x*10, other.y*10, fill="red")
      line2= w.create_line(other.x*10,other.y*10,other2.x*10,other2.y*10,fill="red")
      line3= w.create_line(other2.x*10,other2.y*10,self.x*10,self.y*10, fill="red")
      

def distance(P1, P2):
   distance_x=(P1.x-P2.x)
   temp_x=pow(distance_x,2)
   distance_y=(P1.y-P2.y)
   temp_y=pow(distance_y,2)
   distance = math.sqrt(temp_x+temp_y)
   print "The distance between the points are:", distance

P1 = Point(3,4, "R")
P2 = Point(4,5, "S")
P3= Point(8,10, "T")                
print P1
print P2
print P3

print P1.distance(P2)
P1.triangle(P2,P3)

print "Number of instances created so far:", Point.counter


master.mainloop()







#when we created a non class function for distance. The better way is above (with self and other)
#distance(P1,P2)


##  P1 = Point (5,3)
## ^when you call that, initializing function is automatically called
##  P1.x=5
##  P1.y=3
