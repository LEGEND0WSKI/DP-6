# T: O(n^2)
# S:O(1)
# Leetcode: Yes
# Issues: boundary condition



class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        self.maxi = 0                       # maxlen
        self.start = 0                      # save indexes if bigger maxi
        self.end = 0
        for i in range(n):
            self.extendsAround(s,i,i)       # odd
            if i < n-1 and s[i] == s[i+1]:
                self.extendsAround(s,i,i+1) # even
        return s[self.start:self.end+1]

    def extendsAround(self, s, left, right):
        while left>=0 and right< len(s) and s[left] == s[right]:
            left  -=1
            right +=1
        left  +=1                                   # 1 step back
        right -=1

        if self.maxi < right - left:                # is better than original maximun 
            self.start = left
            self.end = right
            self.maxi = right - left

