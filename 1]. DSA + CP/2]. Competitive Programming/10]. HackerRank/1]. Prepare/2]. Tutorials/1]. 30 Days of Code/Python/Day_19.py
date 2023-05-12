# 20th Solution
#-------------------------------------------------------------------

class AdvancedArithmetic(object):
    def divisorSum(self):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        p = e = 0
        for i in range(1, 1001):
            e = n%i
            if e == 0:
                p += i
        return p

n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print(f"I implemented: {type(my_calculator).__bases__[0].__name__}")
print(s)