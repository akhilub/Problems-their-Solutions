class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(queens, left, right):
            rows = len(queens)
            if n == rows:
                return 1
            ans = 0
            for col in range(n):
                if col not in queens and rows-col not in left and rows+col not in right:
                    ans += dfs(queens + [col], left | {rows- col}, right | {rows + col})
            return ans
        return dfs([], set(), set())

sol=Solution()
print(sol.totalNQueens(8))