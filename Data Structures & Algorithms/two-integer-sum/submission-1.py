class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        snumber={}
        for i,x in enumerate(nums,0):
            req = target - x
            if(req in snumber):
                return [snumber[req], i] 
            else:
                snumber[x] = i