def gcde(a, b, dbg=False):
 """
 standard extended Euclidean algorithm for integers, to get Bezout coefficients.
 Reference Wikipedia
 Note: the function is inconsistent for b=0 or a=0.
 Otherwise it returns a two-tuple: (x,y,d),(u,v)
 with d = gcd(a,b) and
  a*x + b*y == d  AND a*u + b*v == d 
  if x is positive and y negative, then u is negative and v is positive.
 """
 #  a,b = b,a
 if b == 0:
    return (1, 0, a)
 if a == 0:
   return (0,1,b)
 x = [1,0]
 y = [0,1]
 r = [a,b]
 qa = [0,0]
 while r[-1] > 0:
    q, r2 = divmod(r[-2],r[-1])
    r.append(r2)
    x.append(x[-2] - q * x[-1])
    y.append(y[-2] - q * y[-1])
    qa.append(q)
 if dbg:
  print('r=',r)
  print('q=',qa)
  print('x=',x)
  print('y=',y)
 return (x[-2], y[-2], r[-2]),(x[-2]+x[-1], y[-2]+y[-1])

def gcd(a,b):
 (x,y,d),(x1,y1)= gcde(a,b)
 return d

def gcde2(a,b):
 """ 
 applies gcde(a,b) and prints the results in a useful way.
 """
 (x,y,d),(x1,y1)= gcde(a,b)
 print('gcd of %s and %s is %s' %(a,b,d))
 expr = '%s == %s * %s + %s * %s' %(d,a,x,b,y)
 print(expr, eval(expr))
 expr1 = '%s == %s * %s + %s * %s' %(d,a,x1,b,y1)
 print(expr1, eval(expr1))
 
def a_divides_b(a,b):
 """
  Use divmod to divide b by a.
  If the remainder is 0, return the quotient b/a.
  Otherwise return None.
 """
 q,r = divmod(b,a)
 if r == 0:
   return q
 else:
   return None
def gcde3(a,b):
 """
  Assume a,b are positive integers.
  return (x,y,d) where d is greatest common divisor or a,b
  and x,y are positive integers and
  a*x = b*y + d 
  This method uses the gcde function
 """
 (x,y,d),(x1,y1) = gcde(a,b)
 # x*a + y*b = d and x1*a + y1*b = d
 # We choose the case where multiplicand of b is negative
 if y <= 0:
  return (x,-y,d)
 else:
  return (x1,-y1,d)

def gcde3a(a,b,dbg=False):
 """
  Assume a,b are positive integers.
  return (x,y,d) where d is greatest common divisor or a,b
  and x,y are positive integers and
  a*x = b*y + d 
  This method does not use extended Eulidean algorith (gcde),
  but functionally is similar.
  The function is recursive.
  The answer returned may differ from the answer returned by gcde3.
   For example: gcde3(10,6) -> (2,3,2)  (10*2 = 6*3 + 2)
   gcde3a(10,6) -> (5,8,2)  (10*5 = 6*8 + 2).
  gcde3a does not use negative integers.
    It will use x-y but only in contexts where 0<=y<=x.
  Returns None if some problem occurs
 """
 def dbgprint(msg):
  print('%s: %s*%s = %s*%s + %s, gcd(%s,%s) = %s' %(msg,a,x, b,y, d, a,b,d))
 def dbgprint1(msg):
  print('%s: %s*%s = %s*%s + %s, gcd(%s,%s) = %s' %(msg,b,x1, r,y1, d, b,r,d))
 def dbgprint2(msg):
  print('%s: %s*%s = %s*%s + %s, gcd(%s,%s) = %s' %(msg,r,u1, b,v1, d, r,b,d))
 if not ( (type(a) == int) and (type(b) == int) and
          (a>0) and (b>0)):
  # so a>=1 and b>=1
  return None
 q,r = divmod(a,b)  # division algorithm
 # a = b*q + r,  0<=r<b
 if r == 0:
  # a = b*q. So 1 <= q so 0 <= q-1
  x = 1
  y = q - 1
  d = b
  if dbg: dbgprint('A')
  return(x,y,d)
 # r != 0.
 q1,r1 = divmod(b,r)
 # b = r*q1 + r1
 if r1 == 0:
  # b = r*q1 , and so a = (r*q1)*q + r = r*(q1*q + 1) so r divides a.
  # Thus, r == gcd(a,b)
  d = r
  # a*1 = b*q + d
  x = 1
  y = q
  if dbg: dbgprint('B')
  return (x,y,d)
# recursive
 x1,y1,d = gcde3a(b,r,dbg=dbg)
 if dbg:dbgprint1('C1')
 # b*x1 = r*y1 + d
 # Get u1,v1 so r*u1 = b*v1 + d
 # ASSUME: x1<=r and y1<=b
 u1 = b - y1
 v1 = r - x1
 if dbg:dbgprint2('C2')
 # multiply a = b*q + r by u1
 # a*u1 = b*(q*u1) + r*u1
 #      = b*(q*u1) + b*v1 + d
 #      = b*((q*u1) + v1) + d
 # so x = u1, y = q*u1 + v1 satisfies a*x = b*y + d
 x = u1
 y = (q*u1) + v1
 if dbg: dbgprint('C')
 return (x,y,d)

def solve_ax_eq_y(a,b,n):
 """ solve a*x = b (mod n) for x. Return None if no solution
 Intended for a,b,n all non-negative integers
 Uses gcde (extended Euclidean algorithm)
 """
 (x1,y1,d),(x2,y2)= gcde(a,n)
 # a*x1 + n*y1 = d = a*x2 + n*y2
 q,r = divmod(b,d)   
 if r != 0:
   #print('r=',r)
   return None 
 # so d*q = b
 # Almost always, x1>0 and y1 < 0  OR x2 > 0 and y2 < 0
 # Choose the positive x
 if x1 >= 0:
   u = x1
 else:
   u = x2
 # so a*u = d (mod n)
 x = u * q
 return x
def a_inverse(a,n):
 """Solution x of a*x = 1 (mod n). Returns None if no solution"""
 return(solve_ax_eq_y(a,1,n))

def Nsolve0_ax_eq_b(a,b,n,dbg=False):
 """ solve a*x = b (mod n) for x. Return None if no solution
 Require a and n > 0 and b >= 0
 Intended for a,b,n all non-negative integers
 Uses gcde (extended Euclidean algorithm)
 a*x = b + n*y
 Return (x,y). If no solution, return None.
 """
 if (a>0) and (n>0) and (b>=0):
  pass
 else:
  return None
 # Get d as greatest common divisor of a and n
 # a*x1 + n*y1 = d = a*x2 + n*y2  xi,yj are integers
 (x1,y1,d),(x2,y2)= gcde(a,n)
 # Get quotient and remainder for division of b by d
 #     b = d*q + r and 0 <= r < d
 q,r = divmod(b,d)  # divide b by d.
 if r != 0:
  # a*x = b + y*n implies d divides b.
  # r != 0 implies d does not divide b
  return None
 # so d*q = b and r == 0
 if y1 <= 0:
  # a*x1 + n*y1 = d
  x = x1*q
  y = -y1*q
 elif y2 <= 0:
  # a*x2 + n*y2 = d
  x = x2 * q
  y = -y2 * q
 else:
  # this should not happen
  print('ERROR: Nsolve_ax_eq_b(%s,%s,%s)' %(a,b,n))
  return None
 if dbg:
  print('%s*%s == %s + %s*%s' %(a,x,b,n,y))
 return (x,y)
def Nsolve_ax_eq_b(a,b,n,dbg=False):
 """ solve a*x = b (mod n) for x. Return None if no solution
 Require a and n > 0 and b >= 0
 Intended for a,b,n all non-negative integers
 Uses gcde3a (version of extended Euclidean algorithm)
 a*x = b + n*y
 Return (x,y). If no solution, return None.
 """
 if (a>0) and (n>0) and (b>=0):
  pass
 else:
  if dbg: print('No solution found to %s*%s == %s + %s*%s' %(a,'x',b,n,'y'))
  return None
 # Get d as greatest common divisor of a and n
 # a*x1 = n*y1 + d
 (x1,y1,d)= gcde3a(a,n)
 # Get quotient and remainder for division of b by d
 #     b = d*q + r and 0 <= r < d
 q,r = divmod(b,d)  # divide b by d.
 if r != 0:
  # a*x = b + y*n implies d divides b.
  # r != 0 implies d does not divide b
  if dbg: print('No solution found to %s*%s == %s + %s*%s' %(a,'x',b,n,'y'))
  return None
 # so d*q = b and r == 0
 # a*(x1*q) = n*(y1*q) + (d*q) = b
 x = x1*q
 y = y1*q
 if dbg:
  print('%s*%s == %s + %s*%s' %(a,x,b,n,y))
 return (x,y)

def Nmod_inverse(a,n,dbg=False):
 """Solution x of a*x = 1 (mod n).
  Returns None if no solution
  Else returns x,y so that a*x = 1 + n*y (non-negative)
  
 """
 return(Nsolve_ax_eq_b(a,1,n,dbg))

def Nmod(a,b):
 """
 Remainder of division of a by b
 Require a,b to be integers with a>=0 and b>0 (otherwise return None)

 """
 if not ( (type(a) == int) and (type(b) == int) and
          (a>=0) and (b>0)):
  # so b>=1
  return None
 q,r = divmod(a,b)  # division algorithm
 return r

def squares_mod(n):
 """
 returns set of non-zero quadratic residues modulo n.
 Require n to be integer > 1 (otherwise return None).
 """
 if not ( (type(n) == int) and (n>1)):
  return None 
 # so n>=2
 s = {Nmod(x*x,n) for x in range(1,n)}
 # remove 0 if needed.  discard allow possibility that 0 is not in s
 s.discard(0)
 return s

def squareroots_mod(n):
 """
 returns a dictionary whose keys are non-zero quadratic residues modulo n
  and whose values are list of square roots modulo n
 Require n to be integer > 1 (otherwise return {})
 """
 if not ( (type(n) == int) and (n>1)):
  return None 
 # so n>=2
 d = {}
 for x in range(1,n):
  k = Nmod(x*x,n)
  if k not in d:
   d[k] = []
  d[k].append(x)
 # remove 0 as a square  (e.g. 4*4 == 0 mod 8)
 try:
  del d[0]
 except:
  pass
 return d

def pos_squareroots_mod(n):
 """
 returns a dictionary whose keys are non-zero quadratic residues modulo n
  and whose values are list of square roots modulo n
 BUT only include numbers <= n/2
 Require n to be integer > 1 (otherwise return {})
 """
 if not ( (type(n) == int) and (n>1)):
  return None 
 # so n>=2
 d = {}
 halfn = n // 2
 for x in range(1,n):
  k = Nmod(x*x,n)
  if k not in d:
   d[k] = []
  if x <= halfn:
   d[k].append(x)
# remove 0 as a square  (e.g. 4*4 == 0 mod 8)
 try:
  del d[0]
 except:
  pass
 return d

def relprimes(n):
 """ for integer n >= 1, return list of integers 1<=k<=n with
     gcd(k,n) == 1.
     Else return []
 """
 ans = []
 if not ( (type(n) == int) and (n>=1)):
  return []
 if n == 1:
  return [1]
 return [k for k in range(1,n) if gcd(k,n) == 1]

def ephi(n):
 """ Euler's phi function. Cardinality of relprimes(n)
 """
 return len(relprimes(n))

def divisors(n):
 if not ( (type(n) == int) and (n>=1)):
  return []
 return [d for d in range(1,n+1) if (n % d) == 0]

def divisorsum(f,n):
 """
   f a function so f(d) in N
 """
 a = divisors(n)
 s = 0  
 for d in a:
  s = s + f(d)
 return s

def gcdpartition(n):
 """
  1<=n. Returns a Python dictionary, P
  P.keys() = divisors(n)
  P[d] = S(m, 1 <= m <= n and gcd(m,n) == d)
 """
 P = {d:[] for d in divisors(n)} # initialize the partition
 for m in range(1,n+1):
  d = gcd(m,n)
  P[d].append(m)
 return P

def eltOrder(a,n):
 """ 'a' and 'n' integers; 1<=n
  gcd(a,n) = 1
  Find smallest k such that a**k == 1 (mod n)
 """
 if not ( (type(a) == int) and (type(n) == int) and
          (a>0) and (1<=n)):
  return None
 if gcd(a,n) != 1: # gcd in numtheory1
  return None
 k = 1
 x = 1
 while True:
  y = (x*a) % n
  if y == 1:
   return k
  else:
   k = k + 1
   x = y

def ordPartition(n):
 """ 'n' integer, 1<=n
  For a in relprimes(n), find eltOrder(a,n).
  return a dictionary ordpart.  A number d is a key of ordpart
  iff there is a in relprimes(n) with d = ordElement(a).
  ordpart[d] = Set of all a in relprimes(n) such that ordElement(a) = d.
 """
 if not ( (type(n) == int) and (1<=n)):
  return None
 rps = relprimes(n)
 ordpart = {}
 for a in rps:
  d = eltOrder(a,n)
  if d not in ordpart:
   ordpart[d] = []
  ordpart[d].append(a)
 return ordpart

def eltsOfOrder(d,n):
 """ return list of elements of relprimes(n) whose order is d
 """
 return [i for i in relprimes(n) if eltOrder(i,n) == d]

def eltsOfOrderF(n):
 """ Return a function (Python dictionary) whose 
     domain is divisors(ephi(n)) and whose value at d is
     eltsOfOrder(d,n)
 """
 f = {}
 for d in divisors(ephi(n)):
  f[d] = eltsOfOrder(d,n)
 return f

def eltsOfOrderSizeF(n):
 """ Return a function (Python dictionary) whose 
     domain is divisors(ephi(n)) and whose value at d is
     NCard(eltsOfOrder(d,n))
 """
 f = {}
 for d in divisors(ephi(n)):
  f[d] = len(eltsOfOrder(d,n))
 return f

def primRoots(n):
 """ Return list of primitive roots of n
 """
 rp = relprimes(n)
 nrp = len(rp)
 primroots = []
 for k in rp:
  e = eltOrder(k,n)
  if e == nrp:
   primroots.append(k)
 return primroots

def primRootQ(x,n):
 """ Return True or False according to whether
  x is a primitive root of n
 """
 rps = relprimes(n)
 ox = eltOrder(x,n)
 return ox == len(rps)

def primRootIndex(a,r,n):
 """ Return the smallest k (1 <= k <= ephi(n)) and
  r**k = a (mod n)
  Requirements:
  primRootQ(r,n), gcd(a,n) = 1
  Otherwise, return None
 """
 if gcd(a,n) != 1:
  return None
 if not primRootQ(r,n):
  return None
 rps = relprimes(n)
 nrps = len(relprimes(n))  # ephi(n)
 rtok = r  # r**k
 b = a % n 
 for k in range(1,nrps+1):
  if rtok == b:
   return k
  rtok = (rtok*r) % n
 # unexpected:
 return None

def QuadResReps(p):
 """ return list of squares mod p, for p an odd prime
     a^2 mod o for a = 1,...,(p-1)/2
 """
 from prime import isPrime_basic
 if not isPrime_basic(p):
  print('QuadResreps: %s is not a prime' %p)
  return []
 q,r = divmod(p,2)
 if r != 1:
  print('QuadResreps: %s is not odd' %p)
  return []
 q,r = divmod(p-1,2) # Quotient of p-1 by 2
 ans = []
 for a in range(1,q+1):
  q1,qres = divmod(a*a,p)
  ans.append(qres)
 return ans

def test1():
 import sys
 a = int(sys.argv[1])
 b = int(sys.argv[2])
 ans = gcde3a(a,b,dbg=True)
 print('gcde3a(%s,%s) == %s' %(a,b,ans))
 if ans == None:
  return
 x = ans[0]
 y = ans[1]
 d = ans[2]
 expra = '%s*%s' %(a,x)
 exprb = '%s*%s' %(b,y)
 print('%s*%s == %s*%s + %s, gcd(%s,%s) = %s' %(a,x, b,y, d, a,b,d))
 aval = eval(expra)
 bval = eval(exprb)
 flag = (aval == (bval+d))
 print('%s == %s + %s (%s)' %(aval,bval,d,flag))

def test2():
 """
test2: m = 1000. all of 497503 tests passed
test2: m = 10000. all of 49975003 tests passed
 """
 import sys
 m = int(sys.argv[1])
 nok = 0
 ntot = 0
 for a in range(2,m):
  for b in range(a+1,m):
   ntot = ntot + 1
   ans = gcde3a(a,b)
   if ans == None:
    print('None returned for gcde3a(%s,%s)' %(a,b))
    continue
   x,y,d = ans
   if not ( (0 < x) and (x < b) and (0 <= y) and (y < a)):
    print('anomaly: gcde3a(%s,%s) -> (%s,%s,%s)' %(a,b,x,y,d))
    continue
   ans = gcde3a(b,a)
   if ans == None:
    print('None returned for gcde3a(%s,%s)' %(b,a))
    continue
   x,y,d = ans
   if not ( (0 < x) and (x < a) and (0 <= y) and (y < b)):
    print('anomaly: gcde3a(%s,%s) -> (%s,%s,%s)' %(b,a,x,y,d))
    continue
   nok = nok + 1
 if nok == ntot:
  print('test2: m = %s. all of %s tests passed' %(m,ntot))
 else:
  print('test2: m = %s. %s test failed out of %s' %(m,ntot-nok,ntot))

 
if __name__ == "__main__":
 #test1()
 test2()
