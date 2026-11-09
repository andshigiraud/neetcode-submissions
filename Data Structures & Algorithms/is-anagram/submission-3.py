class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countMapS = {}
        countMapT = {}
        for char in s:
            if char not in countMapS:
                countMapS[char] = 1
            else: 
                countMapS[char] +=1
        for char in t:
            if char not in countMapT:
                countMapT[char] = 1
            else: 
                countMapT[char] +=1 
        return countMapS == countMapT
       
"""
if countMapS == countMapT:
            return True
        return False 
"""
       
       
        
            