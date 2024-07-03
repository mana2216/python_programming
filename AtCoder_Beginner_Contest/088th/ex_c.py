def calc_col(c):
    flag_1 = False
    flag_2 = False
    if (c[0][0] - c[0][1]) == (c[1][0] - c[1][1]) and (c[1][0] - c[1][1]) == (c[2][0] - c[2][1]):
        flag_1 = True
    if (c[0][1] - c[0][2]) == (c[1][1] - c[1][2]) and (c[1][1] - c[1][2]) ==  (c[2][1] - c[2][2]):
        flag_2 = True
    if flag_1 and flag_2:
        return True
    else:
        return False

def calc_row(c):
    flag_1 = False
    flag_2 = False
    if (c[0][0] - c[1][0]) == (c[0][1] - c[1][1]) and (c[0][1] - c[1][1]) == (c[0][2] - c[1][2]):
        flag_1 = True
    if (c[1][0] - c[2][0]) == (c[1][1] - c[2][1]) and (c[1][1] - c[2][1]) == (c[1][2] - c[2][2]):
        flag_2 = True
    if flag_1 and flag_2:
        return True
    else:
        return False

c = []
for _ in range(3):
    c.append(list(map(int, input().split())))

if calc_col(c) and calc_row(c):
    print("Yes")
else:
    print("No")