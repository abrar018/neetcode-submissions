class Solution:
    def isValid(self, s: str) -> bool:
        q=[]
        if len(s)==1:
            return False
        for i in s:
            if i in '{[(':
                q.append(i)
            elif i==']' and q and q[-1]=='[' :
                q.pop()
            elif i==')' and q and q[-1] =='(' :
                q.pop()
            elif i=='}' and q and q[-1]=='{' :
                q.pop()
            else:
                return False
        return q==[]