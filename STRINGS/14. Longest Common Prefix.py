class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        retStr=""
        firstStr= strs[0]
        length= len(strs)
        for i in range(len(firstStr)):
            for j in range(1, length):
                if i < len(strs[j]):
                    if firstStr[i] != strs[j][i]:
                        return(retStr)
                else:
                    return(retStr)
            retStr = retStr + firstStr[i]
        
        return(retStr)        
        
        
        
        
        
'''
'Finding longest common prefix'

This can be solved using Brute force And Trie DataStructure
Method-1:

Brute Force:

Pointers method.
1. Place pointers to the given words and then compare them upto the shortest string ..
2. So, this takes O(len(str)*n){n= No. of common elements}
3. Space complexity= O(1) as we are not considering any extra space...
'''

    
