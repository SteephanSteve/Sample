#!/usr/bin/python

n=int(input())
a=raw_input().split(" ")
a.sort()
l=[]
s=[]
for i in a:
    l.append(len(i))
l.sort()
for i in l:
    for j in a:
        if len(j)==i:
            if j not in s:
                s.append(j)
for i in s:
    print i,
