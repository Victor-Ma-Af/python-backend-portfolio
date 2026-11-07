class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if not nums:
            return

        k = k % len(nums)
        nums1 = nums[:]

        position = 0
        giros = 0

        while giros < k:
            while position < len(nums1):
                nums1[position] = nums[position - 1]
                position += 1

            giros += 1
            position = 0
            nums = nums1[:]

        nums[:] = nums1
        return nums

teste = Solution()
nums = [1,2,3,4,5,6,7]

print(teste.rotate(nums, 3))

''' aprimorando com IA
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
'''