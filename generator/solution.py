class Solution:
    def sortedSquares(self, nums):
        result = []
        if len(nums) > 0:
            right = 0

            while right < len(nums) and nums[right] < 0:
                right += 1

            left = right - 1

            while left >= 0 and right < len(nums):
                if abs(nums[right]) < abs(nums[left]):
                    result.append(nums[right]**2)
                    right += 1
                else:
                    result.append(nums[left]**2)
                    left -= 1
            while left >= 0:
                result.append(nums[left]**2)
                left -= 1
            while right < len(nums):
                result.append(nums[right]**2)
                right += 1

        return result
