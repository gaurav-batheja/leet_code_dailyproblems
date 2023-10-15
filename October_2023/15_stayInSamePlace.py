# You have a pointer at index 0 in an array of size arrLen. 
# At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

# Given two integers steps and arrLen, return the number of ways such that your pointer is still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        m = steps
        n = min(steps // 2 + 1, arrLen)

        dp = [[0] * n for _ in range(m + 1)]

        dp[0][0] = 1
        mod = 10 ** 9 + 7

        for i in range(1, m + 1):
            for j in range(n):
                dp[i][j] = dp[i-1][j]  
                if j > 0:
                    dp[i][j] += dp[i-1][j-1]
                if j < n - 1:
                    dp[i][j] += dp[i-1][j+1]

        return dp[m][0] % mod
