class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
            R, C = len(grid), len(grid[0])
            queue = collections.deque()
            visited = set()
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for r in range(R):
                for c in range(C):
                    if grid[r][c] == 0:
                        queue.append((r, c, 0))
                        visited.add((r, c))

            inf = (2 ** 31) - 1

            while queue:
                r, c, d = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        if (nr, nc) not in visited and grid[nr][nc] == inf:
                            grid[nr][nc] = d + 1
                            visited.add ((nr, nc))
                            queue.append((nr, nc, d + 1))
