from collections import Counter
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        c=Counter(A)
        return next((i for i, value in c.items() if value > 1), -1)
