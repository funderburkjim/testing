import sys,re,codecs
from numtheory1 import *
 
def test1():
 a = int(sys.argv[1])
 b = int(sys.argv[2])
 (x1,y1,d),(x2,y2)= gcde(a,b)
 amax = max(abs(x1),abs(x2))
 bmax = max(abs(y1),abs(y2))
 gcde2(a,b) # print ax+by=d formulas
 print('amax=',amax,'bmax=',bmax)


def test2():
 n = int(sys.argv[1])
 # gcde(a,b) for  2 <= b < a <= n
 nok = 0
 nprob = 0
 for a in range(3,n+1):
  for b in range(2,a):
   (x1,y1,d),(x2,y2)= gcde(a,b)
   amax = max(abs(x1),abs(x2))
   bmax = max(abs(y1),abs(y2))
   if (amax < b) and (bmax < a):
    nok = nok + 1
   else:
    print('Surprise at gcde(%s,%s)' %(a,b))
    nprob = nprob + 1
 print(nok,'Hypothesis true')
 print(nprob,'Hypothesis false')

def test3():
 n = int(sys.argv[1])
 # gcde3a(a,b) for  2 <= b < a <= n
 nok = 0
 nprob = 0
 for a in range(3,n+1):
  for b in range(2,a):
   (x1,y1,d)= gcde3a(a,b)
   amax = max(abs(x1),abs(x1))
   bmax = max(abs(y1),abs(y1))
   if (amax < b) and (bmax < a):
    nok = nok + 1
   else:
    print('Surprise at gcde3a(%s,%s)' %(a,b))
    nprob = nprob + 1
 print(nok,'Hypothesis true')
 print(nprob,'Hypothesis false')
if  __name__ ==  "__main__":
 #test1()
 test3()
