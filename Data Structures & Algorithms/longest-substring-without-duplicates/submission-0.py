class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq=[-1]*256
        for i in range(256):
            freq[i] = -1
        l,r,mx,n=0,0,0,len(s)
        while(r<n):
            if(freq[ord(s[r])]!=-1):
                l=max(l,freq[ord(s[r])]+1)
            freq[ord(s[r])] = r
            mxl=r-l+1
            mx=max(mxl,mx)
            r+=1
        return mx