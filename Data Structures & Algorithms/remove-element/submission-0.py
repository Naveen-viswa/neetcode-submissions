class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        temp = []
        for i in nums:
            if i != val :
                temp.append(i)
        #nums = nums[:len(temp)]
        nums[:] = nums[:len(temp)]
        j = 0
        for i in temp:
            nums[j] = i
            j+=1
        return len(nums)