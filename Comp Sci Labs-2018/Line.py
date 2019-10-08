import math
from ClassPoint import *


class Line():
   counter=0

   def __init__(self, P1, P2):
      self.P1 = P1
      self.P2 = P2
      Line.counter +=1

   def __str__(self):
      return "{P1:" + str(self.P1) + " P2:" + str(self.P2) + "}"

   def length(self):
      result= self.P1.distance(self.P2)
      return result


P1= Point(4,5,"X")
P2= Point(1,2,"Y")
print "Point Count:" , Point.counter

L1= Line(P1,P2)
print "Line", L1

print L1.length()

      
