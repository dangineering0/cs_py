class Solution(object):
    # @param n: number of nodes, edges: list of list of edges
    # @return int number of connected comp
    def countComponents(self, n, edges):

        ans = 0


        # adj list
        adj = [[0] * n for y in range(n)]

        for edge in edges:
            adj[edge[1]][edge[0]] = 1

        print adj

        return self.numIslands(adj)

    def numIslands(self, grid):

        ans = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num = grid[i][j]
                if num == 1:
                    self.bfs(i, j, grid)
                    ans += 1

        return ans

    # @param i j and grid
    # @return void
    def bfs(self, i, j, grid):

        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return

        if grid[i][j] == 2 or grid[i][j] == 0:
            return

        grid[i][j] = 2
        self.bfs(i - 1, j, grid)
        self.bfs(i, j - 1, grid)
        self.bfs(i + 1, j, grid)
        self.bfs(i, j + 1, grid)


print Solution().countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]])

