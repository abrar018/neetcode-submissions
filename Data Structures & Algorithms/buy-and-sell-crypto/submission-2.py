class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=1
        l=0
        m=0
        while l<len(prices)-1 and i<len(prices):
            print(l,i)
            m = max(m,prices[i]-prices[l])
            if prices[i]<prices[l]:
                l=i
                i+=1
            else:
                i+=1
        return m