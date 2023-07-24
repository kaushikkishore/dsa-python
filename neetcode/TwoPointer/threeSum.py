from typing import *


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the array first
        nums.sort()

        result = []
        for idx, num in enumerate(nums):
            if idx > 0 and num == nums[idx-1]:
                continue

            left, right = idx+1, len(nums)-1
            while left < right:
                threeSum = num + nums[left] + nums[right]
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])

                    # increase the left pointer so that duplicates are skipped
                    # the right side duplicates will be removed ny the while loop.
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1

        return result

        return result


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))

print(Solution().threeSum([0, 0, 0, 0, 0, 0]))
