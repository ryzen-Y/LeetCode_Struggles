class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        ans = ""
        s = sorted(list(s))

        for i in range(len(s)):

            if target[i] in s:
                ans += target[i]
                s.remove(target[i])

            else:
                for ch in s:
                    if ch > target[i]:
                        ans += ch
                        s.remove(ch)
                        return ans + "".join(s)

                break

        for i in range(len(ans) - 1, -1, -1):

            s.append(ans[i])
            s.sort()

            for ch in s:
                if ch > ans[i]:
                    new_ans = ans[:i] + ch
                    s.remove(ch)

                    return new_ans + "".join(s)

        return ""
