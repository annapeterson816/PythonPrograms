import math

class Date():
   
   def __init__(self,month,day,year):
       self.month = month
       self.day = day
       self.year = year

   def __str__ (self):

      return str(self.month) + "/" + str(self.day) + "/" + str(self.year)

   def isLeapYear(self):
      if self.year %4 == 0:
         return True
      else:
         return False

   def addOneDay(self):
      if self.year%4==0:
         DIM=[31,29,31,30,31,30,31,31,30,31,30,31]
      else:
         DIM=[31,28,31,30,31,30,31,31,30,31,30,31]
         
      max_day= DIM[self.month-1]
      
      if self.day == max_day:
         self.day=1
         if self.month==12:
            self.month=1
            self.year+=1
         else:
            self.month+=1
      else:
         self.day=self.day+1

      return self.day
   
   def addNDays(self, n):
      self.n=n

      DIM=[31,28,31,30,31,30,31,31,30,31,30,31]
      
      for i in range(0,n+1):
         max_day= DIM[self.month-1]
         if self.day == max_day:
            self.day=1
            if self.month==12:
               self.month=1
               self.year+=1
            else:
               self.month+=1
         else:
            self.day=self.day+1

   def subtractTwoDates(self,d2):
      total_days=0
      mon_to_days=0
      diff_in_days=0
      years_to_days=0
      DIM=[31,28,31,30,31,30,31,31,30,31,30,31]

      if d2.year > self.year and abs(d2.year-self.year) >1:
         years_to_days=365*(d2.year-self.year)
      elif d2.year > self.year:
         if d2.month > self.month:
            years_to_days= 365*(d2.year-self.year)
         elif d2.month == self.month:
            if d2.day>self.day:
               year_to_days= 365*(d2.year-self.year)

      if d2.year < self.year and abs(d2.year-self.year) >1:
         years_to_days=365*(d2.year-self.year)
  
      elif d2.year < self.year:
         if d2.month < self.month:
            years_to_days= 365*(d2.year-self.year)
         elif d2.month == self.month:
            if d2.day<self.day:
               year_to_days= 365*(d2.year-self.year)

      if d2.month>self.month:
         for i in range(self.month-1,d2.month):
            mon_to_days+= DIM[i]
      elif d2.month<self.month:
         for i in range(d2.month-1, self.month):
            mon_to_days+= DIM[i]

      dif_in_days = abs(self.day-d2.day)

      total_days=mon_to_days + diff_in_days + years_to_days

      #checking if there was a leapyear
      for j in range(self.year,d2.year):
         if j%4==0:
            total_days+=1
            
      return total_days

   def predictBirthday(self,weekday,thisyear):
      self.weekday=weekday
      self.thisyear=thisyear
      day_index=0

      DOW= ["Monday", "Tuesday", "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]
      i=0
      while i<len(DOW):
         if DOW[i]==self.weekday:
            day_index=i
         i+=1
      
      if thisyear % 4 == 0 or thisyear+1 %4 ==0:
         day_index+=1
         if day_index==7:
            day_index=0
            
      day_index+=1
      if day_index==7:
         day_index=0
      
      return DOW[day_index]         
            
              
d = Date(12,31,2014)
print "The original date is: " , d
print "Is the date a leap year?: " , d.isLeapYear()
d.addOneDay()
print "One day after the original date is: " , d
n=90
d.addNDays(n)
print "After adding" , n, "days, the new date is: " , d
n=30
d.addNDays(n)
print "After adding" , n, "more days, the new date is: " , d

print "\n \n"
d2 = Date(1,15,2016)
print "The original date is: " , d2
print "Is the date a leap year?: " , d2.isLeapYear()
d2.addOneDay()
print "One day after the original date is: " , d2
n=400
d2.addNDays(n)
print "After adding" , n, "days, the new date is: " , d2
print "\n" 
print "The amount of days between" , d , "and", d2 , "is: " , d.subtractTwoDates(d2)

print "\n \n"
d3 = Date(1,27,2013)
print "The original date is: " , d3
print "Is the date a leap year?: " , d3.isLeapYear()
d3.addOneDay()
print "One day after the original date is: " , d3
n=45
d3.addNDays(n)
print "After adding" , n, "days, the new date is: " , d3
n=110
d3.addNDays(n)
print "After adding" , n, "more days, the new date is: " , d3

print "\n \n"
d4 = Date(1,05,2019)
print "The original date is: " , d4
print "Is the date a leap year?: " , d4.isLeapYear()
d4.addOneDay()
print "One day after the original date is: " , d4
n=310
d4.addNDays(n)
print "After adding" , n, "days, the new date is: " , d4
print "\n"

print "The amount of days between" , d3 , "and", d4 , "is: " , d3.subtractTwoDates(d4)

#birthday predictor
print "\n \n"
birth = Date(7,15,1999)
birthday="Saturday"
birthyear=2020
print "Your birthday is:" , birth
print "This year in" , birthyear , "your birthday fell on a" , birthday
print "Next year in" , birthyear+1, "your birthday will fall on a" , birth.predictBirthday(birthday,birthyear)

print "\n \n"
birth2 = Date(9,29,1996)
birthday2="Friday"
birthyear2=2018
print "Your birthday is:" , birth2
print "This year in" , birthyear2, "your birthday fell on a" , birthday2
print "Next year in" , birthyear2+1, "your birthday will fall on a" , birth2.predictBirthday(birthday2,birthyear2)

