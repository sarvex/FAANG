# 1st Solution
from statistics import median
n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
t = len(arr) // 2
U = arr[t:] if len(arr)%2 == 0 else arr[t+1:]
L = arr[:t]
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))

# 2nd Solution
import statistics as st
n = int(input())
data = list(map(int, input().split()))
freq = list(map(int, input().split()))

s = []
for i in range(n):
    s += [data[i]] * freq[i]

N = sum(freq)
s.sort()

q1 = st.median(s[:N//2])
q3 = st.median(s[N//2+1:]) if n%2 != 0 else st.median(s[N//2:])
ir = round(float(q3-q1), 1)
print(ir)


# 3rd Solution
n = int(input().strip())
X = [int(x) for x in input().strip().split()]

mean = sum(X)/n
variance = sum((x - mean) ** 2 for x in X) / n
stddev = variance ** 0.5
print("{0:0.1f}".format(stddev))
