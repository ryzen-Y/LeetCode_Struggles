from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = {}

        for words in strs:
            key = tuple(sorted(words))

            if key not in seen:
                seen[key] = []
            seen[key].append(words)
        return list(seen.values())
