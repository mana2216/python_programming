# 1
d = {}
print(d.get('apple', '-'))

# 2
d = ['o', 'x', '△', 'x', 'o', '△', 'o', 'o', '△', 'x']
d = [item for item in d if item != 'x']
print(d)


# 3
d[0:3] = []
print(d)

# 4
t = ('いろは',)

# 5
d = {'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4}
for key, value in d.items():
    print(f"{key} = {value}")