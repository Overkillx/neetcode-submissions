class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]
        def func(index):
            if index >= len(nums):
                result.append(subset.copy())
                return
            subset.append(nums[index])
            func(index +1 )
            subset.pop()
            func(index+1 )
        func(0)
        return result    