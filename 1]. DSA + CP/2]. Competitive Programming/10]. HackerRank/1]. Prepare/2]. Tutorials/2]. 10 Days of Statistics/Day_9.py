### Day-9
import numpy as np
m,n = [int(i) for i in input().strip().split(' ')]
X = []
Y = []

for _ in range(n):
    data = input().strip().split(' ')
    X.append(data[:m])
    Y.append(data[m:])

q = int(input().strip())
X_new = [input().strip().split(' ') for _ in range(q)]
X = np.array(X,float)
Y = np.array(Y,float)
X_new = np.array(X_new,float)

X_R = X-np.mean(X,axis=0)
Y_R = Y-np.mean(Y)

beta = np.dot(np.linalg.inv(np.dot(X_R.T,X_R)),np.dot(X_R.T,Y_R))

X_new_R = X_new-np.mean(X,axis=0)
Y_new_R = np.dot(X_new_R,beta)
Y_new = Y_new_R + np.mean(Y)

for i in Y_new:
    print(round(float(i),2))
