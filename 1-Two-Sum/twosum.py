"""
sum = target ===> a + b = target ===> a = target - b
"""

from typing import List

# # ! Brute force -> O(n^2)
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for idx1, i in enumerate(nums):
#             for idx2, j in enumerate(nums):
#                 if idx1 != idx2:
#                     if (i + j) == target:
#                         return [idx1, idx2]


# solution = Solution()
# print(solution.twoSum(nums=[3, 3], target=6))


# * Hashmap solution
# Time -> O(n), Space -> O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}  # we will map values : idx
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i


solution = Solution()
print(solution.twoSum(nums=[3, 3], target=6))
