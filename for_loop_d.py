result = 0
for x in range(0, 101):
    if x % 3 == 0: pass
    elif x % 2 == 0:
        result = result + x

print(result)