from Tkinter import*
import tkMessageBox
import math
import random

master = Tk()
master.title("TIC TAC TOE")

board= [None, None, None,None, None, None,None, None, None]
new_move= ''
computer='x'
player='o'
random1=0
winner_key=''
winner=False
bclick= True

def placeMove(board, new_move):
   board[new_move]=player

def isWinner(board):
    #says whether X or O has three in a row
   spots_left=0
   for i in board:
      if i==None:
         spots_left=spots_left+1
   if spots_left==0:
      winner_key='tie'
      winner=True
      return True
      youWin(board, winner_key)
   #diagonal
   elif board[0] == board[4]==board[8] != None :
      winner_key=board[0]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   elif board[2] == board[4]==board[6] != None:
      winner_key=board[2]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   #down
   elif board[0] == board[3]==board[6] != None:
      winner_key=board[0]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   elif board[1] == board[4]==board[7] != None:
      winner_key=board[1]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   elif board[2] == board[5]==board[8] != None:
      winner_key=board[2]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   #across
   elif board[0] == board[1]==board[2] != None:
      winner_key=board[0]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   elif board[3] == board[4]==board[5] != None:
      winner_key=board[3]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   elif board[6] == board[7]==board[8] != None:
      winner_key=board[6]
      winner=True
      print "Player " , winner_key, " Won!"
      return True, winner_key
      youWin(board, winner_key)
   
   else:
      winner=False
      return False

def easy(board):
   random1 = random.randint(0,8)
   if board[random1] != None:
      if winner==False:
         random1=random.randint(0,8)
         return easy(board)
      
   else:
      board[random1]=computer
      return random1

def playAgain(board):
   
   if isWinner(board)== True:
      print "Should call you won!"
      winner_key=isWinner(board)[1]
      youWon(board,winner_key)
      

   elif isWinner(board)==False: 
      print "Here are the taken spots: " , board
      new_move=int(raw_input("What box would you like to go in?"))
      placeMove(board,new_move)
      if isWinner(board)==True:
         winner_key=isWinner(board)[1]
         youWon(board,winner_key)
      else:
         easy(board)
         print "After the computer's turn, the board is now: " , board

         if isWinner(board)==False:
            playAgain(board)
         elif isWinner(board)==True:
            winner_key=isWinner(board)[1]
            youWon(board,winner_key)

#playAgain(board)
      

def tictactoe(buttons):
   global bclick
   if buttons["text"]== " " and bclick==True:
      buttons["text"]= 'x'
      print button0
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
 #     label1= Label(master, text="PLAYER X WON THE GAME", fg="black",bg="lightblue", font=("Arial", 12))
 #     label1.pack()
      
      
      tkMessageBox.showinfo("PLAYER X WON THE GAME")

   elif(button0["text"]=="o" and button1["text"]=="o" and button2["text"]=="o" or
        button0["text"]=="o" and button4["text"]=="o" and button8["text"]=="o" or
        button0["text"]=="o" and button3["text"]=="o" and button6["text"]=="o" or
        button3["text"]=="o" and button4["text"]=="o" and button5["text"]=="o" or
        button6["text"]=="o" and button7["text"]=="o" and button8["text"]=="o" or
        button2["text"]=="o" and button4["text"]=="o" and button6["text"]=="o" or
        button1["text"]=="o" and button4["text"]=="o" and button7["text"]=="o" or
        button2["text"]=="o" and button5["text"]=="o" and button8["text"]=="o"):
      tkMessageBox.showinfo("PLAYER O WON THE GAME")
   
      
buttons=StringVar()

button0=Button(master,text=" ", font=('Arial 30 bold'), highlightbackground='light sea green', fg="black", bg="white",height=4, width=8,command=lambda:tictactoe(button0))
button0.grid(row=1,column=0)


button1=Button(master,text=" ", font=('Arial 30 bold'), highlightbackground='light sea green', height=4, width=8,command=lambda:tictactoe(button1))
button1.grid(row=1,column=1 )

button2=Button(master, text=" ",font=('Arial 30 bold'), highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button2))
button2.grid(row=1,column=2)

button3=Button(master,text=" ", font=('Arial 30 bold'), highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button3))
button3.grid(row=2,column=0)

button4=Button(master,text=" ", font=('Arial 30 bold'), highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button4))
button4.grid(row=2,column=1)

button5=Button(master,text=" ", font=('Arial 30 bold'), highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button5))
button5.grid(row=2,column=2 ,sticky=S+N+E+W)

button6=Button(master, text=" ",font=('Arial 30 bold'), highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button6))
button6.grid(row=3,column=0,sticky=S+N+E+W)

button7=Button(master,text=" ", font=('Arial 30 bold'), highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button7))
button7.grid(row=3,column=1,sticky=S+N+E+W)

button8=Button(master,text=" ", font=('Arial 30 bold') ,highlightbackground='light sea green',height=4, width=8, command=lambda:tictactoe(button8))
button8.grid(row=3,column=2,sticky=S+N+E+W)



master.mainloop()

