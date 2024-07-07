

#print(len(primes_lt_10000),"primes less than 10000")
from primes_lt_1000 import primes_lt_1000 as prime_set
prime_set_max = max(prime_set) # largest precomputed prime
def isPrime(N):
 if N in prime_set:
  return True
 return isPrime_basic(N)

def isPrime_basic(N):
 """
  https://www.pythonforbeginners.com/basics/check-for-prime-number-in-python
 """
 #if N in primes_lt_10000:
 # return True
 if N in [0,1]:
  return False
 if not (type(N) == int):
  return False
 if N <= 0:
  return False
 count = 2
 while count ** 2 <= N:
  if N % count == 0:
   return False
  count = count + 1
 return True

def genprimes(m):
 import codecs
 primes = []
 for n in range(1,m+1):
  if isPrime_basic(n):
   primes.append(n)
 #print('primes <= %s : %s' %(m,primes))
 s = set(primes)
 fileout = "primes_lt_%s.py" %m
 with codecs.open(fileout,"w","utf-8") as f:
  out = 'primes_lt_%s = %s' %(m,s)
  f.write(out+'\n')
 print('write to file %s' %fileout)

def prime_factors(n):
 """
  returns a dictionary 'd' or None
  The dictionary has as keys the prime divisors of 'n'
  and for each such prime 'p', d[p] is the maximum power of p that divides n.
  import math
  math.prod([p**d[p] for p in d]) == n 
 """
 if n >= (prime_set_max*prime_set_max):
  # this algorithm doesn't work
  print('prime_factors fails. Insufficient precomputed primes')
  return None
 n0 = n
 d = {}
 P = []
 while (n0 > 1):
  found = False
  for p in prime_set:
   q,r = divmod(n0,p)
   if r == 0:
    # p divides n0
    if p not in d:
     d[p] = 0
     P.append(p)
    d[p] = d[p] + 1
    n0 = q
    found = True
    break
  if not found:
   # maybe n0 is a prime?
   if isPrime_basic(n0):
    p = n0
    q,r = divmod(n0,p)
    if r == 0:
     # p divides n0
     if p not in d:
      d[p] = 0
      P.append(p)
     d[p] = d[p] + 1
     n0 = q
     found = True
    break
  if not found:
   print('prime_factors error: n0 = %s' % n0)
   return None
 return d

def ephi1(n):
 """ Euler's totient function computed using prime-factorization of n.
 """
 if not ( (type(n) == int) and (n>=1)):
  return 0
 if n == 1:
  return 1
 d = prime_factors(n)
 ans = 1
 for p in d:
  k = d[p]  # p^k
  k1 = k-1
  pk1 = p**k1
  pk = p*pk1 # p^k
  x = pk - pk1
  ans = ans * x
 return ans

def qrinfo(p,q):
 from numtheory1 import pos_squareroots_mod
 if not isPrime(p):
  print('%s not a prime' %p)
  return
 if (p % 2) == 0:
  return '%s not odd' % p
 if not isPrime(q):
  return '%s not a prime' %q
 if (q % 2) == 0:
  return '%s not odd' % q
 if (p == q):
  return '%s and %s are not distinct' %(p,q)
 halfp = (p-1) // 2
 halfq = (q-1) // 2

 if (halfp % 2) == 0:
  ans1 = '%s is semi-even' % p
 else:
  ans1 = '%s is semi-odd' % p
 if (halfq % 2) == 0:
  ans2 = '%s is semi-even' % q
 else:
  ans2 = '%s is semi-odd' % q
 rootsq = pos_squareroots_mod(q)
 p0 = p % q
 if p0 in rootsq:
  rootp = rootsq[p0][0]  # rootsq[p] is a list
  ans3 = '%s is a square of %s (mod %s)' %(p,rootp,q)
 else:
  ans3 = '%s is not a square (mod %s)' %(p,q)
 rootsp = pos_squareroots_mod(p)
 q0 = q % p
 if q0 in rootsp:
  rootq = rootsp[q0][0]  # rootsp[q] is a list
  ans4 = '%s is a square of %s (mod %s)' %(q,rootq,p)
 else:
  ans4 = '%s is not a square (mod %s)' %(q,p)
 ans = ', '. join([ans1,ans2,ans3,ans4])
 return ans


def qr_rec(p,q,ltcode='+',gtcode='-'):
 from numtheory1 import pos_squareroots_mod
 if not isPrime(p):
  print('%s not a prime' %p)
  return
 if (p % 2) == 0:
  return '%s not odd' % p
 if not isPrime(q):
  return '%s not a prime' %q
 if (q % 2) == 0:
  return '%s not odd' % q
 if (p == q):
  return '%s and %s are not distinct' %(p,q)
 halfp = (p-1) // 2
 halfq = (q-1) // 2

 import itertools
 pcoords = range(1,halfp + 1)
 qcoords = range(1,halfq + 1)
 # cartesian product [1..halfp] X [1..halfq]
 cp = list(itertools.product(pcoords,qcoords))
 def flabel(pair,p,q):
  x,y = pair
  if (p*y == q*x):
   return "="
  elif (p*y < q*x):
   return ltcode
  else:
   return gtcode
 #
 def make_lines(p,q):
  ans = []
  for y0 in range(1,1 + halfq):
   y0line = [(x,y,flabel((x,y),p,q)) for (x,y) in cp if y == y0]
   ans.append(y0line)
  return ans
 ans1 = make_lines(p,q)
 # Example: so far
 # qr_rec(5,7)
 # [[(1,1,'^'),(2,1,'^')],[(1,2,'>'),(2,2,'^')],[(1,3,'>'),(2,3,'>')]]

 # column totals (# of py < qx)
 coltots = []
 for x in range(1, 1 + halfp):
  tot = 0
  for y in range(1, 1 + halfq):
   # cf. flabel function
   if (p*y < q*x) :
    tot = tot + 1
  coltots.append(tot)
 # row totals (# of py > qx)
 rowtots = []
 for y in range(1, 1 + halfq):
  tot = 0
  for x in range(1, 1 + halfp):
   # cf. flabel function
   if (p*y > q*x) :
    tot = tot + 1
  rowtots.append(tot)
  # ans2 = ans1[::-1]
 def make_lines1(p,q):
  lines = make_lines(p,q)
  ans = []
  for iline,line in enumerate(lines):
   newline = [code for (x,y,code) in line]
   text = '  '.join(newline)
   text1 = '%3d %s #- %d' %(iline+1,text, rowtots[iline])
   ans.append(text1)
  ansrev = ans[::-1]  # reverse
  
  # add a line for the 'p' (x-coord)
  xcoord = []
  for i in range(0,1+halfp):
   if i == 0:
    xcoord.append('  ') # don't show the 0
   else:
    xcoord.append('%3d' % i)
  xcoord1 = ''.join(xcoord)
  ansrev.append(xcoord1)
  # add a line for number of '+' in columns
  colwork = []
  for coltot in coltots:
   colwork.append('%3d' % coltot)
  colwork1 = ''.join(colwork)
  colwork1 = '#+' + colwork1
  ansrev.append(colwork1)
  # sum summary
  arow = sum(rowtots)
  acol = sum(coltots)
  outarr = []
  outarr.append('p = %s, halfp = %s, #+ = %s' % (p,halfp,acol))
  outarr.append('q = %s, halfq = %s, #- = %s' % (q,halfq,arow))

  a = qrinfo(p,q).split(',')
  for x in a:
   outarr.append(x)
  for out in outarr:
   ansrev.append(out)
  # a bit more
  temptxt = """
the quadratic reciprocity theorem can be phrased:

 IF either p or q is semi-even, THEN
  p is a square mod q IFF q is a square mod p
 IF both p and q are semi-odd, THEN
  p is a square mod q IFF q is not a square mod p 
  AND
  p is not a square mod q IFF q is a square mod p
"""
  for line in temptxt.splitlines():
   ansrev.append(line)
  ansall = '\n'.join(ansrev)
  print(ansall)
  return

 make_lines1(p,q)
 #return ans
if __name__ == "__main__":
 #test1(10)
 pass
