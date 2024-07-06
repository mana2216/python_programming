sets1 = set([2, 4, 8, 16, 32])
sets2 = set([1, 10, 4, 16])

print(sets1.union(sets2))
sets3 = {str(i) for i in sets1 if i > 5}
print(sets3)