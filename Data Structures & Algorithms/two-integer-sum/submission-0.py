class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        possible = {}
        ans = []
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in possible:
                ans.append(possible[rem])
                ans.append(i)
                return ans
            else:
                possible[nums[i]] = i 