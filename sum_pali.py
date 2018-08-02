#!/usr/bin/python

n=list(raw_input())
n=sum(map(int,n))
n=str(n)
if n==n[::-1]:
    print "YES"
else:
    print "NO"
