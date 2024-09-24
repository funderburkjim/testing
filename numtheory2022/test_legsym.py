"""
"""
def legsym(a,p):
 from numtheory1 import QuadResReps, gcd
 """ p is an odd prime
     a an integer (not necessarily positive)
     gcd(a,p) = 1
 """
 squares = QuadResReps(p)
 if (squares == []):
  print('legsym: Cannot find Quadratic residues of mod %s' %p)
  return None
 if (gcd(a,p) != 1):
  print('legsym: %s and %s are not relatively prime' % (a,p))
  return None
 q,r = divmod(a,p)
 if r in squares:
  return 1
 else:
  return -1

def test_legsym():
 import sys
 a = int(sys.argv[1])
 p = int(sys.argv[2])
 ans = legsym(a,p)
 print(ans)

def legsym_table_helper(p,q,a,b,c):
 out1 = 'QR(%2d,%2d)=%2d' % (q,p,a)
 out2 = 'QR(%2d,%2d)=%2d' % (p,q,b)
 out = '%s %s %2d' %(out1,out2,c)
 return out
def legsym_table_helper1(p,q,a,b,c,nperm):
 out1 = 'QR(%2d,%2d)=%2d' % (q,p,a)
 out2 = 'QR(%2d,%2d)=%2d' % (p,q,b)
 out = '%s %s %2d %2d' %(out1,out2,c,nperm)
 return out
def legsym_table(m):
 from prime import isPrime
 # fileout = sys.argv[1]
 #m = 40
 nout = 0
 for p in range(3,m):
  if not isPrime(p):
   continue
  phalf,_ = divmod(p-1,2)
  for q in range(3,p):
   if not isPrime(q):
    continue
   qhalf,_ = divmod(q-1,2)
   a = legsym(q,p)
   b = legsym(p,q)
   c = (-1)** (phalf * qhalf)
   assert a*c == b  # gauss quadratic reciprocity theorm
   out = legsym_table_helper(p,q,a,b,c)
   nout = nout + 1
   print(out)
 print('m=%s, nout=%s' % (m,nout))

def legsym_table1(m):
 from prime import isPrime
 # fileout = sys.argv[1]
 nout = 0
 for p in range(3,m):
  if not isPrime(p):
   continue
  phalf,_ = divmod(p-1,2)
  for q in range(3,p):
   if not isPrime(q):
    continue
   qhalf,_ = divmod(q-1,2)
   a = legsym(q,p)
   b = legsym(p,q)
   c = (-1)** (phalf * qhalf)
   assert a*c == b  # gauss quadratic reciprocity theorm
   out = legsym_table_helper(p,q,a,b,c)
   nout = nout + 1
   print(out)
   domain,perm,nperm = pqperm(p,q)
   print('pqperm(%s,%s):' %(p,q))
   print(domain)
   print(perm)
   print(nperm)
   domain,perm,nperm = pqperm(q,p)
   print('pqperm(%s,%s):' %(q,p))
   print(domain)
   print(perm)
   print(nperm)
   print()
 print('m=%s, nout=%s' % (m,nout))

def pqperm(p,q):
 """
  k*q mod(p) for k=1,...,(p-1)/2
 """
 phalf,_ = divmod(p-1,2)
 qhalf,_ = divmod(q-1,2)
 domain = []
 perm = []
 n = 0
 for k in range(1,p):
  x,r = divmod(k*q,p)
  domain.append(k)
  perm.append(r)
  if k <= phalf:
   if r > phalf:
    n = n + 1
 return(domain,perm,n)
def test_pqperm():
 import sys
 q = int(sys.argv[1])
 p = int(sys.argv[2])
 domain,perm,n = pqperm(p,q)
 print(domain)
 print(perm)
 print(n)

if __name__ == "__main__":
 # test_legsym()
 # test_pqperm()
 legsym_table1(12)
 
