grid = []
N = int(input())
for _ in range(N):
    grid.append(list(input()))

for i in range(N-2, -1, -1):
    for j in range(2*N-1):
        if grid[i][j] == "#" and j-1 >= 0 and grid[i+1][j-1] == "X":
            grid[i][j] = "X"
        if grid[i][j] == "#" and grid[i+1][j] == "X":
            grid[i][j] = "X"
        if grid[i][j] == "#" and j+1 <= 2*N-1 and grid[i+1][j+1] == "X":
            grid[i][j] = "X"

for i in range(len(grid)):
    for j in range(len(grid[0])):
        print(grid[i][j], end="")
    print()