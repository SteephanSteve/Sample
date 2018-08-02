#!/usr/bin/python

def out(s,f,l):
   if f==l:
      x=int(''.join(s))
      if x not in a and x>int(n):
         a.append(x)
   else:
      for i in range(f,l+1):
         s[i],s[l]=s[l],s[i]
         out(s,f+1,l)
         s[i],s[l]=s[l],s[i]
n=raw_input()
s=list(n)
a=[]
out(s,0,len(s)-1)
if a:
   print min(map(int,a))
else:
   print "impossible"
