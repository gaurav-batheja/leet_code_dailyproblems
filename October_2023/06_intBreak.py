# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.

class Solution:
    def integerBreak(self, n: int) -> int:
        if n==2 or n==3:
            return n-1
        elif n==4:
            return 4
        elif n==5:
            return 6
        elif n==6:
            return 9
        else:
            m=n%3
            n=(n-m)/3
            return int(max(3**(n-1)*2*(m+1),3**n,3**(n)*m))
