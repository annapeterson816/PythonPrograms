from Tkinter import *

x,y=200,200
radius=60

def drawRings(radius, x,y):
   the_canvas.create_oval(
   

def innerRingsHelper(n):
   if n==0:
      return 0
   else:
      innerRingsHelper(x,y,radius, n)
      print "yes"

     
def innerRings(x,y,radius, n):
   p1_x,p1_y= x-radius, y-radius
   p2_x, p2_y =x+radius, y+radius

   if (n%2==0):
      the_canvas.create_oval(p1_x+n, p1_y+n,p2_x-n, p2_y-n, fill='light blue')
      print "light blueee"
   else:
      the_canvas.create_oval(p1_x+n, p1_y+n,p2_x-n, p2_y-n, fill='white')
      
   if n>5:
      #innerRings(n-5)
      innerRingsHelper(x,y,radius,n-5)


      
   



window= Tk()
window.title("Inner Rings")
the_canvas=Canvas(window, width=400, height=400)
the_canvas.grid(row=0, column=0)


innerRings(60)
window.mainloop()
