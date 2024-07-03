# 1
data = [1, 2, -3, 3]
for item in data:
    print(item)

# 2
for i in range(1, 101):
    print(i)

# 3
data2 = [item * 10 for item in data]

# 4
tmp_list = [item for item in data if item >= 0]
total_data = sum(tmp_list)

# 5
num = 20
if 10 <= num < 50:
    print(num)