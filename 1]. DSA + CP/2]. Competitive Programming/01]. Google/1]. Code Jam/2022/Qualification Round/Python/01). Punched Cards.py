def solve(r,c):
    r = int(r)
    c = int(c)
    for i in range (1,r*2 +2):
        for j in range (1,c*2 + 2):
            if i in [1, 2] and j in [1, 2]:
                print('.', end ="")
            elif(i % 2 == 1 and j % 2 == 1):
                print('+', end ="")
            elif(i % 2 == 0 and j % 2 == 1):
                print('|', end ="")
            elif(i % 2 == 1 and j % 2 == 0):
                print('-', end ="")
            elif(i % 2 == 0 and j % 2 == 0):
                print('.', end ="")
        print( )

test_num = int(input())
r=[0] * test_num
c=[0] * test_num
for i in range (test_num):
    r[i],c[i] = input().split()
for i in range (0,len(r)):
    print(f"Case #{str(i + 1)}:")
    solve(r[i],c[i])


