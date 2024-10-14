my_dict = {
    "name":"john",
    "age":25,
    "weight":"80kg"
}

print(my_dict)

weight = my_dict["weight"]

print(weight)

my_dict["height"] = "100"

print(my_dict)

del my_dict["height"]
print(my_dict)

number_list = ["1", "2", "3", "4", "5"]
letter_list = ["A", "B", "C", "D", "E"]
"""
makes 3x " on either side makes multi lined comment
dict(zip(x, y)) turns two lists into a dict?
"""
new_dict = dict(zip(number_list, letter_list))
print(new_dict)