class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        occurance = {}
        isExist = False
        for x in nums:
            if x in occurance and occurance[x]==1:
                isExist = True
                break
            occurance[x] = occurance.get(x,0)+1
        return isExist