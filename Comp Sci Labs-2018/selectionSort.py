##missing something, does not work

def selectionSort(L):
   for j in range(0, len(L)-1):
      minVal=L[j]
      minIndex=j
      for k in range(j+1,len(L)):
         if L[k]<minVal:
            minValue=L[k]
            minIndex = k
      L[minIndex]=L[j]
      L[j]=minVal

      print L

L2= [10,4,7,2,40,0,9,6,66,69,72,79,8]

import time
start_time=time.time()
selectionSort(L2)
print "Time in seconds", (time.time()-start_time)
      
