import math
for i in range(int(input())):
    q=input().split()
    print(int(math.sqrt(int(q[0])*float(q[1])/3600)*2500/2))
