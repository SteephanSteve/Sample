#!/usr/bin/python

s1,s2,k=raw_input().split(' ')
k=int(k)
c=abs(len(s1)-len(s2))
for i in range(min(len(s1),len(s2))):
    if not s1[i]==s2[i]:
        c+=1
if c==k: print 'yes' 
else: print "no"   
