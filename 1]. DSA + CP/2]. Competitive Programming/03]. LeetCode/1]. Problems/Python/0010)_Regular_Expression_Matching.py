class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        matched = [[False for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        matched[0][0] = True

        for i in range(len(s)+1):
            for j in range(1, len(p)+1):
                pattern = p[j-1]

                if pattern == '*':
                    star = p[j-2]
                    matched[i][j] = (
                        matched[i][j - 2]
                        or i > 0
                        and matched[i - 1][j]
                        and star in [s[i - 1], '.']
                    )

                elif pattern == '.':
                    matched[i][j] = (i != 0 and matched[i-1][j-1])

                else:
                    matched[i][j] = (i != 0 and matched[i-1][j-1] and s[i-1] == pattern)
        return matched[-1][-1]