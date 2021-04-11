class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dir = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        @lru_cache(None)
        def dfs(i,j) -> int:
            ans=1
            for d in dir:
                if 0<=i+d[0]<m and 0<=j+d[1]<n and matrix[i+d[0]][j+d[1]]>matrix[i][j]:
                    ans = max(ans, dfs(i+d[0],j+d[1])+1)
            return ans
        
        return max(dfs(i,j) for i,j in product(range(m),range(n)))
