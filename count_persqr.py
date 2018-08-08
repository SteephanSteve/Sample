#!/usr/bin/python

l,r=map(int,raw_input().split(' '))
def persqr(n):
    s=0
    i=1
    while s<n:
        s+= i
        if s == n:
            return True
        i += 2
c=0
for n in range(l,r):
    if persqr(n):
        c+=1
print c
    

