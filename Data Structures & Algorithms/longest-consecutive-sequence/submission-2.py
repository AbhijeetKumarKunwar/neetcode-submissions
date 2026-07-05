class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0
        for n in nums:
            #if n is the starting of any subsequence which means it does not
            #have any n-1 in the data set,we will go till we get the consicutive sub sequecen
            if n-1 not in numSet:
                length=0
                while n+length in numSet:
                    length+=1
                longest=max(length,longest)
        return longest         

                
                
