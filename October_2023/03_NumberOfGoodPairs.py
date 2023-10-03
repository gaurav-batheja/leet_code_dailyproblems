"""
1512. Number of Good Pairs
Given an array of integers nums, return the number of good pairs.
A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        j,goodpair=0,0
        for i in nums:
            goodpair+=nums[j+1::].count(i)
            j+=1
        return goodpair
