class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=1
        count=0
        for i,n in enumerate(nums):
            if n!=0:
                result*=n
            else:
                nonZeroProduct=i
                count+=1        
        if count>=2:
            nums[:]=len(nums)*[0]
            return nums;
        if count==1:
            nums[:]=len(nums)*[0]
            print(nums)
            nums[nonZeroProduct]=result
            return nums

        for i in range(0,len(nums)):
            if nums[i]!=0:
                nums[i]=result//nums[i]
        return nums    