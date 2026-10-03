class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        res=0
        Hashset=set()
        l=0

        for r in range(len(s)):
            while s[r] in Hashset:
                Hashset.remove(s[l])
                l=l+1
            Hashset.add(s[r])
            res=max(res,r-l+1)
        return res


        
        