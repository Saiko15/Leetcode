class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n, m = len(triangle), 1
        
        @cache
        def solve(c,r):
            # base condition when we move further from the last row.
            if r == n:
                return 0
            
            # base condition when we go out of bounds
            if c < 0 or c >= len(triangle[r]):
                return float('inf')
            
            # after selecting the cell in the current row, then in the next row i can select either the col with the same index or index + 1
            return triangle[r][c] + min(solve(c, r+1),solve(c+1, r+1))
            
        return solve(0,0)