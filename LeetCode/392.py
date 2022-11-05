from typing import List
"""
sol: comparing index
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0 #index of subsequence
        n=len(s)
        m = len(t)

        if n>m: # sub leng can't greater than original text
            return False
        for j in t:
            if i == n:  #index leng == sub leng
                return True
            if s[i]==j: #comparing chars
                i=i+1 #sub index increasing
        return n==i




s='acd'
t='ahbgdc'
sol= Solution()
print(sol.isSubsequence(s,t))