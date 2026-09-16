class Solution:
    def findMin(self, nums: List[int]) -> int:
        right = len(nums) -1
        left = 0

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left == right

        return nums[left]