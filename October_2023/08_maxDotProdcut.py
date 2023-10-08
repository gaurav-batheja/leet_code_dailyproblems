# Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters.
# (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).

class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        memo = [[float('-inf')] * m for _ in range(n)]
        
        def dp(i, j):
            if i == n or j == m:
                return float('-inf')
            
            if memo[i][j] != float('-inf'):
                return memo[i][j]
            
            memo[i][j] = max(
                nums1[i] * nums2[j] + max(dp(i + 1, j + 1), 0),
                dp(i + 1, j),  
                dp(i, j + 1), 
            )
            
            return memo[i][j]
        
        return dp(0, 0)
