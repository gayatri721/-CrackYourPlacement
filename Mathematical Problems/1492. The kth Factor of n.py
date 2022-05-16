class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n+1):
            if n % i == 0:
                k -= 1
                if k == 0:  #  No need to find more than kth  factor, we can simply return it  once we reached.
                    return i
        return -1
