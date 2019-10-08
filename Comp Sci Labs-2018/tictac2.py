from Tkinter import*
import tkMessageBox



master = Tk()
master.title("TIC TAC TOE")
w = Canvas(master, width=600, height=600)
#w.pack()
w.create_rectangle(0, 0, 600, 600, fill="light sea green", width = 5, outline = "cyan4")
w.create_line(0, 200, 600, 200, fill = "cyan4", width = 5)
w.create_line(0, 400, 600, 400, fill = "cyan4", width = 5)
w.create_line(200, 0, 200, 600, fill = "cyan4", width = 5)
w.create_line(400, 0, 400, 800, fill = "cyan4", width = 5)


bclick= True


def tictactoe(buttons):
   global bclick
   if buttons["text"]== " " and bclick==True:
      buttons["text"]= 'x'
      bclick=False
   elif buttons["text"]== " " and bclick==False:
      buttons["text"]="o"
      bclick=True
      
   elif(button0["text"]=="x" and button1["text"]=="x" and button2["text"]=="x" or
        button0["text"]=="x" and button4["text"]=="x" and button8["text"]=="x" or
        button0["text"]=="x" and button3["text"]=="x" and button6["text"]=="x" or
        button3["text"]=="x" and button4["text"]=="x" and button5["text"]=="x" or
        button6["text"]=="x" and button7["text"]=="x" and button8["text"]=="x" or
        button2["text"]=="x" and button4["text"]=="x" and button6["text"]=="x" or
        button1["text"]=="x" and button4["text"]=="x" and button7["text"]=="x" or
        button2["text"]=="x" and button5["text"]=="x" and button8["text"]=="x"):
      tkMessageBox.showinfo("PLAYER X WON THE GAME")

   elif(button1["text"]=="o" and button2["text"]=="o" and button3["text"]=="o" or
        button1["text"]=="o" and button5["text"]=="o" and button9["text"]=="o" or
        button1["text"]=="o" and button4["text"]=="o" and button7["text"]=="o" or
        button4["text"]=="o" and button5["text"]=="o" and button6["text"]=="o" or
        button7["text"]=="o" and button8["text"]=="o" and button9["text"]=="o" or
        button3["text"]=="o" and button5["text"]=="o" and button7["text"]=="o" or
        button2["text"]=="o" and button5["text"]=="o" and button8["text"]=="o" or
        button3["text"]=="o" and button6["text"]=="o" and button9["text"]=="o"):
      tkMessageBox.showinfo("PLAYER O WON THE GAME")
   
      
buttons=StringVar()

button0=Button(master, text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button0))
button0.grid(row=1,column=0,sticky=S+N+E+W)

button1=Button(master,text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button1))
button1.grid(row=1,column=1,sticky=S+N+E+W)

button2=Button(master, text=" ",font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button2))
button2.grid(row=1,column=2,sticky=S+N+E+W)

button3=Button(master,text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button3))
button3.grid(row=2,column=0,sticky=S+N+E+W)

button4=Button(master,text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button4))
button4.grid(row=2,column=1,sticky=S+N+E+W)

button5=Button(master,text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button5))
button5.grid(row=2,column=2,sticky=S+N+E+W)

button6=Button(master, text=" ",font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button6))
button6.grid(row=3,column=0,sticky=S+N+E+W)

button7=Button(master,text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button7))
button7.grid(row=3,column=1,sticky=S+N+E+W)

button8=Button(master,text=" ", font=('Arial 30 bold'),height=4, width=8, command=lambda:tictactoe(button8))
button8.grid(row=3,column=2,sticky=S+N+E+W)

#tictactoe(buttons)

master.mainloop()

