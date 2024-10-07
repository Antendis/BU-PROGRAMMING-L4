a = 11
a += 5
a_type = type(a)
print(a, " is a the type ", a_type)

b = 16
b /= 2 # use // for int
print(b, " is type ", type(b))

c = 2.5 # is a float
print(int(c)) # can be changed to int

tom_marvolo_riddle = "Tom Riddle"

print(tom_marvolo_riddle[:3].upper()) # the [] chooses which part of the string, the .upper makes it all upprercase
print(tom_marvolo_riddle[-6:].lower()) 

# tom_marvolo_riddle[0] = "I"
# test above didnt work because strings are immutable?

print(tom_marvolo_riddle.replace("Tom", "Vol"))
print(tom_marvolo_riddle.replace("Tom Ri", "Voldem "))
print(tom_marvolo_riddle.replace("Tom Riddle", "Lord Voldemort"))



