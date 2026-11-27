class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d={}
        e={}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            d[s[i]]=1+d.get(s[i],0)
            e[t[i]]=1+e.get(t[i],0)
        return d==e
            