import math
import random

board= [None, None, None,None, None, None,None, None, None]
new_move= ''
computer='x'
player='o'
random1=0
winner_key=''
winner=False

##if mode=='easy':
##   easy(board)
##elif mode=='medium':
##   medium()

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
         easy(board)
      
   else:
      board[random1]=computer
      print "The computer's move is: " , random1, " \n"


def youWon(board,winner_key):
   print winner_key
   if winner_key == player:
      return "You win!"
   elif winner_key == computer:
      return "You lost :("
   else:
      return "cats game!"
   


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
         print "Should call you won!"
         winner_key=isWinner(board)[1]
         youWon(board,winner_key)
      else:
         easy(board)
         print "After the computer's turn, the board is now: " , board

         if isWinner(board)==False:
            playAgain(board)
         elif isWinner(board)==True:
            print "Should call you won!"
            winner_key=isWinner(board)[1]
            youWon(board,winner_key)
  
         


   
playAgain(board)   


   


#medium level 



##def medium(board):
##   #for the columns
##   for i in board:
##      count=0
##      for j in board[i]:
##         if j==player:
##            count=count+1
##      if count==2:
##         for char in board:
##            if char==None:
##               char=computer
##
##   #for rows
##   num=0
##   for k in range(0,3):
##      count=0
##      for j in range(0,3):
##         if board[j,k]==player:
##            count=count+1
##      if count==2:
##         for char in board:
##            if char==None:
##               char=computer
##      
##   return board



