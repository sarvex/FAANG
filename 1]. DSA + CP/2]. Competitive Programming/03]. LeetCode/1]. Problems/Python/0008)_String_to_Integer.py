class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        negative = False
        if str:
            if str[0] == '-':
                negative = True
            if str[0] in ['+', '-']:
                str = str[1:]
        if not str:
            return 0

        digits = set('0123456789')
        result = 0
        for c in str:
            if c not in digits:
                break
            result = result*10 +int(c)

        if negative:
            result = -result

        return max(min(result, 2**31-1), -2**31)