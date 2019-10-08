#volume of a sphere

radius= raw_input("what is the radius of the sphere?")

radius = int(radius)

import math

four_thirds= float(4)/float(3)


volume = four_thirds * radius**3 * math.pi


print volume



#price per book

copies = raw_input("How many copies do you want?")

copies = float(copies)

price = (24.95)*(.60)*copies + (3) + (.75)*(copies-1)

print price


#running time

after_1_mile = 7.0015

new_time = after_1_mile + 3*(.0712) + 0.815

new_time = str(new_time)

print "\n \n" + new_time
