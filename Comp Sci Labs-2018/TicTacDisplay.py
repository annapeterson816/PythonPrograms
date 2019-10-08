from Tkinter import *


window= Tk()
window.title("Tic Tac Toe")
the_canvas=Canvas(window, width=400, height=400, 'light blue')
the_canvas.grid(row=0, column=0)



#needs to be the last line on any code that you are trying to display 
window.mainloop()
