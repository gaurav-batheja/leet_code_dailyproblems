# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        return [x for x in list(set(nums)) if nums.count(x)>len(nums)//3]
