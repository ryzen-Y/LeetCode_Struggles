class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        target = n // 3
        seen = {}
        ll = []

        for i in range(n):

            seen[nums[i]] = seen.get(nums[i] , 0 ) + 1

            if seen[nums[i]] > target and nums[i]not in ll:
                ll.append(nums[i])
            

        return ll
            
        