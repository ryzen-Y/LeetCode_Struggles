class Solution:
    def minMoves(self, nums: list[int]) -> int:
        maximum = max(nums)
        move = 0  

        for i in range(len(nums)):
            if nums[i] == maximum:
                continue
            sub = 0
            sub = maximum - nums[i]
            move += sub 
            
        return move  
        