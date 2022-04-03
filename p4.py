
import sys
from math import sqrt

lo = 50000
hi = 100000

cnt = 0
for i in range(lo,hi+1):
    s = sqrt( sqrt(i) )
    x = s % 1
    if x > 0.93:
        cnt += 1
        # print(i,s,x)
print(cnt)
