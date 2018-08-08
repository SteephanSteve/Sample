#!/usr/bin/python

def gcd(a,b):
    if a==b:
        return a
    elif a>b:
        return gcd(a-b,b)
    return gcd(a,b-a)
a=map(int,raw_input().split(" "))
g=gcd(a[0],a[1])
for i in a:
    g=gcd(g,i)
print g
