
# You are given an n x n integer matrix grid.
# Generate an integer matrix maxLocal of size (n - 2) x (n - 2) such that:
# maxLocal[i][j] is equal to the largest value of the 3 x 3 matrix in grid centered around row i + 1 and column j + 1.


from itertools import chain

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        ans = [[0]*(len(grid)-2) for _ in range(len(grid)-2)]
        for i in range(len(grid)-2):
            for j in range(len(grid)-2):
                ans[i][j] = max(chain(grid[i][j:j+3], grid[i+1][j:j+3], grid[i+2][j:j+3]))
        return ans

