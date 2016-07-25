# @input list of list of str
# @return int of unique islands

def numIslands(grid):

    ans = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            num = grid[i][j]
            if num == '1':
                bfs(i,j,grid)
                ans +=1

    return ans

# @param i j and grid
# @return void
def bfs(i,j,grid):

    if i < 0 or i >= len(grid):
        return
    if j < 0 or j >= len(grid[0]):
        return

    if grid[i][j] == '2' or grid[i][j] == '0':
        return

    grid[i][j] = '2'
    bfs(i-1, j, grid)
    bfs(i, j-1, grid)
    bfs(i+1, j, grid)
    bfs(i, j+1, grid)


y = ["11000",
    "11000",
    "00100",
    "00011"]
g = [list(x) for x in y]
print g

print numIslands(g)