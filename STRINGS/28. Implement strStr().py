class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(needle==""):
            return 0
        i,j=0,0
        while(i<len(haystack) and j<len(needle)):
            if(haystack[i]==needle[j]):
                i=i+1
                j=j+1
                if(j==len(needle)):
                    return i-len(needle)  
            else:
                i=i-j+1  
                j=0  
        return -1
