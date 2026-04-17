class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            d[i] = 1+ d.get(i,0)

        print(d)
        l=[]

        val = sorted(list(d.values()))[-k:]
        
        for i in d:
            if d[i] in val:
                l.append(i)
        return l
        