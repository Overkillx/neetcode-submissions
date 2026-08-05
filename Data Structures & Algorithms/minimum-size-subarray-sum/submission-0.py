class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=[]
        for i in range(len(nums)):
            temp = []
            for j in range(i, len(nums)):
                temp.append(nums[j])
                if sum(temp) >= target:
                    res.append(len(temp))
                    break  
        return min(res) if res else 0


        