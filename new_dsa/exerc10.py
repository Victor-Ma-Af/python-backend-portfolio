class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for num in nums[:]:
            if num == 0: nums.append(num), nums.remove(num)