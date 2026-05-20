class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        self.lists = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        self.rows = len(grid)
        self.cols = len(grid[0])

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and self.lists[y][x] != "1":
                    self.searchGrid(grid, x, y)
                    islands += 1

        return islands
    
    def searchGrid(self, grid: List[List[str]], x: int, y: int) -> None:
        q = deque()

        self.lists[y][x] = "1"
        q.append((y, x))

        while q:
            row, col = q.popleft()

            dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]

            for dr, dc in dirs:
                r, c = row + dr, col + dc
                if (r in range(self.rows) and c in range(self.cols) and grid[r][c] == "1" and 
                    self.lists[r][c] != "1"):
                    q.append((r, c))
                    self.lists[r][c] = "1"
