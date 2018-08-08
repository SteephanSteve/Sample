#!/usr/bin/python

n=int(input())
a=raw_input().split(" ")
a.sort()
l=[]
for i in a:
    l.append(len(i))
l.sort()
for i in l:
    for j in a:
        if len(j)==i:
            print j,
