class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
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
        