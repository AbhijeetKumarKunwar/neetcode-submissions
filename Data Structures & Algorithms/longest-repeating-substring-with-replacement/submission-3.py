class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        has=[0]*26
        l,maxCharCount,sm=0,0,0
        for r in range(len(s)):
            has[ord(s[r])-ord('A')]+=1
            maxCharCount=max(maxCharCount,has[ord(s[r])-ord('A')])
            if(((r-l+1)-maxCharCount)>k):
                has[ord(s[l])-ord('A')]-=1
                l+=1
            sm=max(sm,r-l+1)
        return sm


        