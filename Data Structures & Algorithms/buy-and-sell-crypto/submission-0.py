class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i= 0
        maxp=0
        while i<len(prices)-1:
            if prices[i+1]<prices[i]:
                i+=1
                continue
            j=i+1
            while j<len(prices):
                if prices[j]>prices[i]:
                    maxp = max(prices[j]-prices[i],maxp)
                j+=1
            i+=1
        return maxp
        