from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # brute force/naive soluton: search through the entire 2d grid (already O(n^2)) and figure out of all fruits can become rotten and count the number of minutes possibly per iteration -> worse than O(n^2) -> O(n^3)
        # proposed solution: Run a BFS from every rotten fruit in the grid and calculate the time. We will iterate the number of minutes per level that we iterate when running the BFS.

        R, C = len(grid), len(grid[0])
        q = deque() # queue containing the vertices tuples: (i, j) used for BFS. Can have at most all vertices so spcae is O(n * m)
        total, count, minutes = 0, 0, 0

        for i in range(len(grid)): # O(n * m)
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += 1 # total fresh fruit (to compare against count calculated from BFS)
                if grid[i][j] == 2:
                    q.append((i, j)) # append the vertices that are rotting oranges

        while q:
            level = len(q)
            if count > 0:
                minutes += 1

            for i in range(level):
                x1, y1 = q.popleft() # grab rotten fruit (x, y)
                for x2, y2 in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    r, c = x1 + x2, y1 + y2
                    if r >= 0 and r < R and c >= 0 and c < C and grid[r][c] == 1:
                        q.append((r, c))
                        count += 1
                        grid[r][c] = 2 # make the fruit rotten so it cant be repushed into the queue

        return minutes if count == total else -1

        # time: O(n * m), space: O(n * m)