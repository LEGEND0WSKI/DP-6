# T: O(n^2)
# S:O(1)/O(n) for array / O(n^2) for matrix dp
# Leetcode: Yes
# Issues: boundary condition



# dp array 1309 ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [False]*n
        start, end = 0,0

        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i-j <= 1 or dp[j+1]:
                        dp[j] = True
                        if end - start < i-j:
                            start = j
                            end = i
                    else:
                        dp[j] = False
                else:
                    dp[j] = False

        return s[start:end+1]

# dp matrix 1792 ms

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False]*n for i in range(n)]
        start, end = 0,0

        for i in range(n):
            for j in range(i+1):
                if s[i] == s[j]:
                    if i-j <= 1 or dp[i-1][j+1]:
                        dp[i][j] = True
                        if end - start < i-j:
                            start = j
                            end = i
                    else:
                        dp[i][j] = False
                else:
                    dp[i][j] = False

        return s[start:end+1]
#  246 ms 
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

