class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False
        
        
        
        """
        countMap = {}
        for n in nums:
            if n not in countMap:
                countMap[n] = 1
            elif n in countMap:
                countMap[n] += 1
            if countMap[n] >= 2:
                return True
        return False
        """
        