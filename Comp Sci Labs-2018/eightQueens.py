def isSafe(board, row):
   print "Inside isSafe function"
   print "Board", board, "Row", row
   if row in board:
      print "return False"
      return False

   for col in range(len(board)):
      print "Col: " , col
      if row-board[col]==len(board)-col:
         print "return False"
         return False
      if row-board[col]==col-len(board):  ## just a reverse of this, finds diagonals both going up and going down
         print "return False"
         return False

   print "return True"
   return True
   


def eightQueens(size, board):
   if size > len(board):
      for j in range(size):  #check each row, 0,1,2,3
         if isSafe(board, j):
            newBoard = board+(j,)
            result= eightQueens(size, newBoard)
            if result!= None:
               return result

   else:
      return board


      
print eightQueens(4, tuple())
