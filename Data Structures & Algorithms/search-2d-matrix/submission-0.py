class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in range(len(matrix)):
            l, r = 0, len(matrix[0]) - 1

            while l <= r:
                m = l + ((r - l) // 2)
                val = matrix[row][m]

                if val < target:
                    l = m + 1
                elif val > target:
                    r = m - 1
                else:
                    return True
        return False