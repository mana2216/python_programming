total = 0
i = 0
while (i < 101):
    i += 1
    if i % 2 != 0:
        continue
    total += i

print(f"合計値は{total}です。")