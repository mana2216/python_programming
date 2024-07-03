from collections import defaultdict
S = input()
person_dict = defaultdict(int)
for p in S:
    person_dict[p] += 1

print(max(person_dict, key=person_dict.get))