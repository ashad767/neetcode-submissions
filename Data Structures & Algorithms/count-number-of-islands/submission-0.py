class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        self.lists = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1" and self.lists[y][x] != "1":
                    self.searchGrid(grid, x, y)
                    islands += 1

        return islands
    
    def searchGrid(self, grid: List[List[str]], x: int, y: int) -> None:
        if y >= len(grid) or x >= len(grid[0]) or grid[y][x] == "0" or self.lists[y][x] == "1":
            return
        print(y,x)
        self.lists[y][x] = "1"

        if y < len(grid) - 1 and grid[y + 1][x] == "1":
            self.searchGrid(grid, x, y+1)
        
        if x < len(grid[0]) - 1 and grid[y][x+1] == "1":
            self.searchGrid(grid, x+1, y)
        
        if y > 0 and grid[y - 1][x] == "1":
            self.searchGrid(grid, x, y-1)
        
        if x > 0 and grid[y][x-1] == "1":
            self.searchGrid(grid, x-1, y)