from Tkinter import *

def drawRing(the_canvas, x,y,radius, width, color):
   p1_x,p1_y= x-radius, y-radius
   p2_x, p2_y =x+radius, y+radius
   #outer ring
   the_canvas.create_oval(p1_x, p1_y,p2_x, p2_y, fill=color)
   #inner ring
   the_canvas.create_oval(p1_x+width, p1_y+width,p2_x-width, p2_y-width, fill='white')
   top = Tk()
   L1 = Label(top, text="User Name")
   L1.pack( side = LEFT)
   E1 = Entry(top, bd =5)
   E1.pack(side = RIGHT)


window= Tk()
window.title("Rings")
the_canvas=Canvas(window, width=400, height=400)
the_canvas.grid(row=0, column=0)

drawRing(the_canvas, 200,200,150,60, "light blue")


#needs to be the last line on any code that you are trying to display 
window.mainloop()
