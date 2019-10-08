def merge(list1, list2):
   mergelist=[]
   i=0
   j=0
   while i<len(list1) and j<len(list2):
      if list1[i]<list2[j]:
         mergelist.append(list1[i])
         i=i+1
      else:
         mergelist.append(list2[j])
         j=j+1
   mergelist+=list1[i:]
   mergelist+=list2[j:]

   return mergelist

def mergeSort(L):
   mergeSortHelper(L,0,len(L)-1)

   return L

def mergeSortHelper(L,i,j):
   if i<j:
      mid=(i+j)/2
      mergeSortHelper(L, i, mid)
      mergeSortHelper(L, mid+1,j)
      L[i:j+1]=merge(L[i:mid+1],L[mid+1:j+1])


L= merge([3,7,5,12,36,79],[45,32,12,10,6])
print "The merged list is: ", L

import time
start_time=time.time()
print "After the merge list is sorted: ", mergeSort(L), " \n Time to sort: ", (time.time()-start_time), " seconds"
