grid = []
for i in range(3):
    a_list = list(map(int, input().split()))
    grid.append(a_list)

N = int(input())
bingo = [["o" for _ in range(3)] for _ in range(3)]
for _ in range(N):
    B = int(input())
    pos1 = -1
    pos2 = -1
    for i in range(3):
        if B in grid[i]:
            pos1 = i
            pos2 = grid[i].index(B)
    if pos1 != -1 and pos2 != -1:
        bingo[pos1][pos2] = "x"

flag = False

if bingo[0][0] == "x" and bingo[0][1] == "x" and bingo[0][2] == "x":
    flag = True
elif bingo[1][0] == "x" and bingo[1][1] == "x" and bingo[1][2] == "x":
    flag = True
elif bingo[2][0] == "x" and bingo[2][1] == "x" and bingo[2][2] == "x":
    flag = True
elif bingo[0][0] == "x" and bingo[1][0] == "x" and bingo[2][0] == "x":
    flag = True
elif bingo[0][1] == "x" and bingo[1][1] == "x" and bingo[2][1] == "x":
    flag = True
elif bingo[0][2] == "x" and bingo[1][2] == "x" and bingo[2][2] == "x":
    flag = True
elif bingo[0][0] == "x" and bingo[1][1] == "x" and bingo[2][2] == "x":
    flag = True
elif bingo[0][2] == "x" and bingo[1][1] == "x" and bingo[2][0] == "x":
    flag = True
else:
    flag = False

if flag:
    print("Yes")
else:
    print("No")