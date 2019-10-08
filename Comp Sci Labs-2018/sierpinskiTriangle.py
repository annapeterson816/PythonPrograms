from Tkinter import *

def drawTriangle(p1,p2,p3):
   the_canvas.create_polygon([p1,p2,p3], fill = 'blue', width=5)

def sierpinskiHelper ( n , p1, p2, p3 ) :
   if n == 1 :
      drawTriangle(p1, p2, p3)

   else :
      p4 = ((p1[0]+p2[0])/2,(p1[1]+p2[1])/2)
      p5 = ((p2[0]+p3[0])/2,(p2[1]+p3[1])/2)
      p6 = ((p3[0]+p1[0])/2,(p3[1]+p1[1])/2)

      sierpinskiHelper ( n-1 , p1, p4, p6)
      sierpinskiHelper ( n-1 , p4, p2, p5)
      sierpinskiHelper ( n-1 , p6, p5, p3)

window= Tk()
window.title("Sierpinski Triangles")
the_canvas=Canvas(window, width=400, height=400)
the_canvas.grid(row=0, column=0)

sierpinskiHelper(5,(0,0),(200,400), (400,0))


#needs to be the last line on any code that you are trying to display 
window.mainloop()
