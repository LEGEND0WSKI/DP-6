# Time:O(nlogn)
# Space:O(n) pq
# Leetcode:Yes
# Issues:No


# ugly numbers create ugly children 3^n
import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        hset = set()
        prime = {2,3,5}
        pq = []
        currUgly = 1

        heapq.heappush(pq,currUgly)
        hset.add(currUgly)

        while n>0:
            currUgly = heapq.heappop(pq)        # 5

            for p in prime:
                newUgly = currUgly * p
                if newUgly not in hset:
                    heapq.heappush(pq, newUgly) # 10,15,25
                    hset.add(newUgly)
            n-=1

        return currUgly
            