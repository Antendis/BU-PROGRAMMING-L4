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

too_many_spaces = "            space      "
print(too_many_spaces)
no_spaces = too_many_spaces.strip() # removes outside spaces
print(no_spaces)

python_java = "Python java C++"
print(python_java.split()) # splits string into list where each word is an item

print(tom_marvolo_riddle.replace("Tom", "Vol"))
print(tom_marvolo_riddle.replace("Tom Ri", "Voldem "))
print(tom_marvolo_riddle.replace("Tom Riddle", "Lord Voldemort"))

potassium = "Bananas are great source of Potassium"
print(potassium.count("a"))





