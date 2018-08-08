#!/usr/bin/python

a=[]
for i in range(3):
    x=raw_input().split(' ')
    a.append(map(int,x))
c=0
for i in range(3):
    if i<3-1:
      if a[i][0]==a[i+1][0] or a[i][1]==a[i+1][1]:
          c+=1
      else:
          print "no"
          break
if c==2:
    print "yes"          
