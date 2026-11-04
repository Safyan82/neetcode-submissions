class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # here the solution for this
        # first solution is if we do count each element and sort base on freq
        # in desc order then we can get the top k element 
        # this solution comes under nlogn times

        # but we can do it for n times opertion mean linear time

        # like we will have an array of size of the list elements
        # like if we have length of 6 we will have the array of 6 + 1 = 7

        # now we will count the elements and see the frequency
        # while traversing the dict and getting their frequency
        # we will append those number like 5 have 2 frequency we wiill
        # append that 5 under the array/list index 2 and append it mean
        # we have the array list under the index 2 all numbers that occurs
        # 2 times comes in that array 


        if k<=len(nums):

            freqC = Counter(nums)
            arr = [[] for _ in range(len(nums)+1)]

            for ke, v in freqC.items():
                arr[v].append(ke) 

            finalNum = []

            for i in range(len(arr)-1, 0 , -1):
                
                for num in arr[i]:    
                            # take every number in the bucket, not just [0]
                    finalNum.append(num)

                    if len(finalNum) == k:
                        return finalNum


            return finalNum

