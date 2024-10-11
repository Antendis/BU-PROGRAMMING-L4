num = input("Give me a number: ")
num = int(num)

i = 0

while i < num:
  i += 1
  spacelen = num - i
  given = i
  print(" " * spacelen, str(given) * i)
