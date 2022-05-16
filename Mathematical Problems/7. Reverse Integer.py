class Solution:
    def reverse(self, x: int) -> int:
        res=int(str(abs(x))[::-1])
        if res>=2**31: return 0
        return res if x>=0 else -res
