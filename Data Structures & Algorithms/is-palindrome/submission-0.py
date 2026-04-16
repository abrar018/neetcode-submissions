class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lis=[]
        l=0
        m=''.join(x.lower() for x in s if x.isalnum())
        r=len(m)-1
        while l<=r:
            if m[l]!=m[r]:
                return False
            l+=1
            r-=1
        return True

        