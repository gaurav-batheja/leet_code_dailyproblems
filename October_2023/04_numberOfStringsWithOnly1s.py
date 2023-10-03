# Given a binary string s, return the number of substrings with all characters 1's. 
# Since the answer may be too large, return it modulo 109 + 7.

class Solution:
    def numSub(self, s: str) -> int:
        s=s.split("0")
        sums=0
        for i in s:
            if i!="":
                sums+=(int(len(i)*(len(i)+1)/2))
        return sums%(10**9+7)
