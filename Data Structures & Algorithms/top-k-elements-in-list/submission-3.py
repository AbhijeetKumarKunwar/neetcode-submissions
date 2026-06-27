# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         dic={}
#         for num in nums:
#             if num not in dic:
#                 dic[num]=1
#             else:
#                 dic[num]+=1
#         dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
#         nums=[x[0]  for x in dic]    
#         return nums[:k]
        
#from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        freq=[[] for i in range(0,len(nums)+1)]  #[[],[],[],,,,n]    
        #this is to calculate the lis of numers having coun equal to its index of list
        for num in nums:
            dic[num]=1+dic.get(num,0)
        for num,count in dic.items():
            freq[count].append(num)
        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
