import collections


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        d = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        q = collections.deque(list(d[digits[0]]))
        for ch in digits[1:]:
            new_q = []
            letters = d[ch]
            while q:
                start = q.popleft()
                new_q.extend(start + j for j in letters)
            q = collections.deque(new_q)
        return q
