# class Solution:
#     def containsDuplicate(self, nums: list[int]) -> bool:
#         return len(nums) > len(set(nums))


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums) in [0, 1]:
            return False

        hashset = set()
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False


solution = Solution()
nums = [1, 2, 3, 1]
print(solution.containsDuplicate(nums))
