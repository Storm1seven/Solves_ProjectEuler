grid = []
ans = []
for _ in range(20):
	grid.append(list(map(int, input().split())))
for i in grid:
	for j in range(3, 20):
		ans.append(i[j-3]*i[j-2]*i[j-1]*i[j])
for i in range(3, 20):
	for j in range(20):
		ans.append(grid[j][i-3]*grid[j][i-2]*grid[j][i-1]*grid[j][i])
for i in range(17):
	for j in range(17):
		ans.append(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3])
for i in range(3, 20):
	for j in range(17):
		ans.append(grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3])
print(max(ans))