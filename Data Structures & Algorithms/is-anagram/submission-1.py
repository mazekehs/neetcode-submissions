class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
        #O(nlogn)-> time
        #O(1)-> space
        