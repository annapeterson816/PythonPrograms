from Tkinter import *

window= Tk()
window.title("Rings")
the_canvas=Canvas(window, width=400, height=400)
the_canvas.grid(row=0, column=0)

the_canvas.create_polygon([400,400,200,200,400,0], fill="yellow", width=5)

window.mainloop()
