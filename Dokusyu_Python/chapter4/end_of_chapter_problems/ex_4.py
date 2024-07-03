total = 0
for i in range(100, 201):
    if i % 2 == 0:
        continue
    total += i

print(total)