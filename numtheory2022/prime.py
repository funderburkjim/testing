

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
 
if __name__ == "__main__":
 #test1(10)
 pass
