from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        O(m * n * 26)
        """
        res = defaultdict(list)  # mapping charCount to list of Anagrams

        for word in strs:
            count = [0] * 26  # a ... z

            for char in word:
                # correct offset for mapping, a -> 0
                count[ord(char) - ord("a")] += 1
            # convert to tuple bcoz list cannot be keys
            res[tuple(count)].append(word)

        return list(res.values())


solution = Solution()
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
res = solution.groupAnagrams(strs)
print(res)
