from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Brute force solution => O(m * nlog(n))
        """

        if len(strs) == 0 or len(strs) == 1:
            return List[strs]
        else:
            anagrams = {}
            for word in strs:
                sorted_word = "".join(sorted(word))
                if sorted_word in anagrams:
                    anagrams[sorted_word].append(word)
                else:
                    anagrams[sorted_word] = [word]

        res = []
        for group in anagrams.values():
            res.append(group)

        return res


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = solution.groupAnagrams(strs)
print(res)
