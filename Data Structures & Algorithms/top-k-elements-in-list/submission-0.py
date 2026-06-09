class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        retn={}
        freq=[]

        for i in nums:
            if i not in retn:
                retn[i]=1
            else:
                retn[i]+=1
        check=dict(sorted(retn.items(), key = lambda item: item[1], reverse = True))
        final_check= list(check.items())

        for i in range(k):
            freq.append(final_check[i][0])        
        return freq    

        