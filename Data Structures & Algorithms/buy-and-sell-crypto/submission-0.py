class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r,mx=0,0,0
        while(r<len(prices)):
            if(prices[r]<prices[l]):
                l=r
                r+=1
            else:
                mx=max(mx,prices[r]-prices[l])
                r+=1
        return mx        



