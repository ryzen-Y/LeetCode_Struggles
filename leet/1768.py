class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = min(len(word1), len(word2))
        s = ""

        for i in range(n):
            s = s + word1[i] + word2[i]

        if len(word1) > len(word2):
            s = s + word1[n:]
        else:
            s = s + word2[n:]

        return s


# ======= Two pointers ======

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        s = ""

        word1_len = len(word1)
        word2_len = len(word2)

        while i < word1_len or j < word2_len:

            if i < word1_len:
                s = s + word1[i]
                i += 1
            if j < word2_len:
                s = s + word2[j]
                j += 1
        return s
