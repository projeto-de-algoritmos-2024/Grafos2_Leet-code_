class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def is_valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        def count_islands(grid_copy):
            count = 0
            visited = set()

            def dfs(r, c):
                if (r, c) in visited or not is_valid(r, c) or grid_copy[r][c] == 0:
                    return
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)

            for r in range(rows):
                for c in range(cols):
                    if grid_copy[r][c] == 1 and (r, c) not in visited:
                        dfs(r, c)
                        count += 1
            return count

        initial_islands = count_islands(grid)

        if initial_islands == 0 or initial_islands > 1:
            return 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    grid_copy = [row[:] for row in grid] 
                    grid_copy[r][c] = 0
                    if count_islands(grid_copy) > 1 or count_islands(grid_copy) == 0:
                        return 1
        return 2




