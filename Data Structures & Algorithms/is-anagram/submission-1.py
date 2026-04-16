class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        e={}
        f={}
        for i in range(len(s)):
            e[s[i]] = e.get(s[i],0)+1
            f[t[i]] = f.get(t[i],0)+1
        return e==f