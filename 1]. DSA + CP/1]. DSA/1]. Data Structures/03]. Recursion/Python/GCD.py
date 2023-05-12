#finding gcd of 2 numbers recursively
def gcd(a,b):
    return a if b==0 else gcd(b, a%b)

a = 10
b = 4
if a>b:
    a,b = b,a
print(gcd(a,b))