def binarySearch(L, element):
   low=0
   high=len(L)-1

   while(low<=high):
      mid= (low+high)/2
      print "low, mid, high: ", low, mid, high
      if (L[mid]==element):
         return True, mid
      
      elif L[mid]<element:
            low=mid+1

      else:
            high=mid-1

   return False


L=[2,4,7,10,45,50,59,60,66,69,71,79,80]
element=61
print L
print "element", element
print binarySearch(L, element)
