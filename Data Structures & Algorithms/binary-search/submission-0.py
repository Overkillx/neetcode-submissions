class Solution:
    def search(self, nums: List[int], target: int) -> int:
        a= -1
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            else:
                if target not in nums:
                    return a
        