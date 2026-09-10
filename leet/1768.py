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
        len_one = len(word1)
        len_two = len(word2)

        while i < len_one or j < len_two:

            if i < len_one:
                s = s + word1[i]
                i += 1
            if j < len_two:
                s = s + word2[j]
                j += 1
        return s
