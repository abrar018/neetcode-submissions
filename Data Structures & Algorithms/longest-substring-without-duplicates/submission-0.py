class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=set()
        m=0
        l=0
        for r in range(len(s)):
            while s[r] in n:
                n.remove(s[l])
                l+=1
            n.add(s[r])
            m=max(m,len(n))
        return m
            
        