num = input("Give me a number: ")
num = init(num)

i = 0

while i < num:
  i += 1
  spacelen = num - 1
  given = i
  print(" " * spacelen, str(given) * i)
