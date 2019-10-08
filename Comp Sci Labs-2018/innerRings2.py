from Tkinter import *

x,y=200,200
radius=60
width=50
color='light blue'

def drawRings(p1_x, ):
   the_canvas.create_oval(p1_x, p1_y,p2_x, p2_y, fill=color)
   

def innerRingsHelper(n, x,y,radius):
   if n==1:
      
   
      drawRings(p1_x,p1_y,p2_x,p2_y)

   else:
      p1_x,p1_y= x-radius, y-radius
   p2_x, p2_y =x+radius, y+radius
      innerRingsHelper(n-1, p1_x+width, p1_y+width,p2_x-width, p2_y-width)



innerRingsHelper(8, (200,200), (100,100), (0,0))

window= Tk()
window.title("Inner Rings")
the_canvas=Canvas(window, width=400, height=400)
the_canvas.grid(row=0, column=0)


window.mainloop()
