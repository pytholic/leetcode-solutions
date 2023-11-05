# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False

#         count_s, count_t = {}, {}
#         for i in range(len(s)):
#             count_s[s[i]] = 1 + count_s.get(
#                 s[i], 0
#             )  # "get" to avoid key errors
#             count_t[t[i]] = 1 + count_t.get(t[i], 0)
#         for ch in count_s:
#             if count_s[ch] != count_t.get(ch, 0):
#                 return False
#         return True


# solution = Solution()
# print(solution.isAnagram(s="anagram", t="nagaram"))


# # ? Can we do O(1)
# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         # interviewers assume sortign does not take space
#         return sorted(s) == sorted(t)


# # * I do not need two dicts
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}
        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)
            count[t[i]] = count.get(t[i], 0) - 1
        for c in count:
            if count[c] != 0:
                return False
        return True
