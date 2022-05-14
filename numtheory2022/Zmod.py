
class Zmod:
 @staticmethod
 def generate(base):
  return [Zmod(i,base) for i in range(0,base)]

 @staticmethod
 def zero(base):
  return Zmod(0,base)
  
 @staticmethod
 def one(base):
  return Zmod(1,base)

 @staticmethod
 def relprimes(base):
  import numtheory1
  a = numtheory1.relprimes(base)
  ans = [Zmod(i,base) for i in a]
  return ans
 
 def __init__(self,n,base):
  # n assumed an int (Integer, positive or negative)
  # base (the modulus) assumed integer > 0
  self.base = base
  self.n = self.normalize(n)
  #c = self.__class__ # class constructor

 def __repr__(self):
  return '%d (mod %d)' %(self.n,self.base)
 
 def normalize(cls,n):
  q,r = divmod(n,cls.base)
  return r

 def mult_inverse(self):
  from numtheory1 import Nmod_inverse
  a = Nmod_inverse(self.n,self.base)
  if a == None:
   print('%s has no multiplicative inverse modulo %s' %(n,cls.base))
   return 0  # questionable. Maybe should raise exception
  ans,r = a  # r == 1
  return Zmod(ans,self.base)
 
 def __add__(self,other):
  """ implement binary '+' 
  """
  if self.base != other.base:
   print('Cannot add %s, %s' %(self,other))
   return None
  x = self.n
  y = other.n
  z = self.normalize(x+y)
  c = self.__class__ # class constructor
  return c(z,self.base)
 
 def __sub__(self,other):
  """ implement binary '-' 
  """
  if self.base != other.base:
   print('Cannot subtract %s, %s' %(self,other))
   return None
  x = self.n
  y = other.n
  z = self.normalize(x-y)
  c = self.__class__ # class constructor
  return c(z,self.base)
 
 def __neg__(self):
  """ unary '-' for Zmod objects
  """
  x = self.n
  z = self.normalize(-x)
  c = self.__class__ # class constructor
  return c(z,self.base)
 
 def __mul__(self,other):
  """ implement binary '*' 
  """
  if self.base != other.base:
   print('Cannot multiply %s, %s' %(self,other))
   return None
  x = self.n
  y = other.n
  z = self.normalize(x*y)
  c = self.__class__ # class constructor
  return c(z,self.base)
 
 def __eq__(self,other):
  """ implement binary ==
  """
  return (self.n == other.n)

 def __truediv__(self,other):
  """ implement binary division /
   a*u = b (mod m)
   u = b*v (mod m) where v = b/a
  """
  if self.base != other.base:
   print('Cannot divide %s, %s' %(self,other))
   return None
  y1 = other.mult_inverse()
  return self*y1
    
 def pow(self,k):
  # k>=0
  p = pow(self.n,k,self.base)
  return Zmod(p,self.base)
 
"""
ZmodPoly
a simple implementation of polynomials with coefficients in Z/mZ
 (integers mod m)
The coefficients are assumed to be 

"""

class ZmodPoly(object):
 @staticmethod
 def zero(base):
  return ZmodPoly([Zmod.zero(base)],base,Zmod)
  
 @staticmethod
 def one(base):
  return ZmodPoly([Zmod.one(base)],base,Zmod)

 @staticmethod
 def monomial(n,base):
  """ X^n """
  if ((type(n) == int) and (0<=n) and
      (type(base) == int) and (0<base) ):
   zero = Zmod.zero(base)
   one =  Zmod.one(base)
   # example n=3.  [zero,zero,zero,one]
   a = [zero]*(n+1)
   a[n] = one
   ans = ZmodPoly(a,base,Zmod)
   return ans
  else:
   print('ZmodPoly.monomial ERROR: n=%s, base=%s' %(n,base))
   return None
  return ZmodPoly([Zmod.one(base)],base,Zmod)

 @staticmethod
 def divstep(a,b):
  """ a and b are ZmodPoly objects with same base.
      Do one step of division of a by b.
      returning q,r so a = b*q + r and deg(r) < deg(a)
      Return None if some problem
  """
  dbg = False
  base = a.base
  if base != b.base:
   print('ZmodPoly.divstep fails: two bases %s %s' %(a.base,b.base))
   print('a = %s' % a)
   print('b = %s' % b)
   return None
  da = a.deg()
  db = b.deg()
  if da < db:
   q = ZmodPoly.zero(base)
   r = b
   return (q,r)
  # db <= da 
  # b = b1*X^db and a = a1*X^da
  # dc := da - db
  # c1 := a1/b1  # c1 is in Zmod so  a1 = b1*c1
  # q1 := c1*X^dc
  # r1 := a - b*q1
  dc = da - db
  Xdc = ZmodPoly.monomial(dc,base)
  a1 = a.coeffs[da].n
  b1 = b.coeffs[db].n
  if dbg:
   print('a = %s' % a)
   print('b = %s' % b)
   print('da = %s' % da)
   print('db = %s' % db)
   print('dc = %s' % dc)
   print('Xdc= %s' % Xdc)
   print('Xdc.coeffs = %s' % Xdc.coeffs)
   print('a1 = %s' %a1)
   print('b1 = %s' %b1)
  # solve for c1
  from numtheory1 import Nsolve_ax_eq_b
  temp = Nsolve_ax_eq_b(b1,a1,base)
  if temp == None:
   print('ZmodPoly.divstep fails. Cannot divide %s by %s modulo %s' %(a1,b1,base))
   return None
  (q_,y_) = temp  # a1 = b1*q_ + y_  (in N
  if dbg:
   print('q_ = %s, y_=%s' % (q_,y_))
  q1 = Xdc
  q1.coeffs[dc] = Zmod(q_,base)
  r1 = a - b*q1
  if dbg:
   print('q1 = %s' %q1)
   print('r1 = %s' %r1)
  return(q1,r1)

 def __init__(self,numlist,base,numclass=int):
  """numlist is a (non-empty) sequence of integers (the coefficients)
     base is a positive integer - the base of modular arithmetic
     numclass is expected to be either int or Zmod
  """
  self.base = base
  if numclass == int:
   self.coeffs = [Zmod(i,base) for i in numlist]
  else:
   self.coeffs = numlist
  self.zero = Zmod.zero(base)
  self.one = Zmod.one(base)
  self.normalize()

 def __repr__(self):
  X = 'X'
  a = []
  for i,c in enumerate(self.coeffs):
   a.append("%d%s%d" %(c.n,X,i))
  s1 = ' + '.join(a)
  ans = '%s (mod %s)' %(s1,self.base)
  return ans
 
 def deg(self):
  """ degree of ZmodPoly object
  """
  d = 0 # the degree What about the zero polynomial ? should this be -1?
  for i,a in enumerate(self.coeffs):
   if not (a == self.zero):
    d = i
  return d

 def normalize(self):
  d = self.deg()
  self.coeffs = self.coeffs[0:d+1]  # remove higher power with 0 coefficients

 def __add__(self,other):
  """ implement binary '+' for ZmodPoly objects
  """
  if self.base != other.base:
   print('Cannot add %s, %s' %(self,other))
   return None
  x = self.coeffs
  y = other.coeffs  # assume to have same base
  base = self.base
  nx = len(x)
  ny = len(y)
  m = max(nx,ny)
  z = [] # array of Zmod objects
  zero = self.zero
  for i in range(m):
   # use ternary operator
   a = x[i] if (i < nx) else zero
   b = y[i] if (i < ny) else zero
   z.append(a+b)
  return ZmodPoly(z,base,numclass=Zmod)

 def __sub__(self,other):
  """ implement binary '-' for ZmodPoly objects
  """
  if self.base != other.base:
   print('Cannot subtract %s, %s' %(self,other))
   return None
  x = self.coeffs
  y = other.coeffs  # assume to have same base
  base = self.base
  nx = len(x)
  ny = len(y)
  m = max(nx,ny)
  z = [] # array of Zmod objects
  zero = self.zero
  for i in range(m):
   # use ternary operator
   a = x[i] if (i < nx) else zero
   b = y[i] if (i < ny) else zero
   z.append(a-b)
  return ZmodPoly(z,base,numclass=Zmod)

 def __neg__(self):
  """ unary '-' for ZmodPoly objects
  """
  x = self.coeffs
  base = self.base
  #nx = len(x)
  z = [-c for c in x]  # c is a Zmod object
  return ZmodPoly(z,base,numclass=Zmod)

 def scalarprod(self,k):
  """ k assumed to be int
   self.coeffs is list of Zmod objects
  """
  base = self.base
  k1 = Zmod(k,base)
  z = [k1*c for c in self.coeffs]
  return ZmodPoly(z,base,numclass=Zmod)
 
 def __mul__(self,other):
  """ binary '*' for Zmodpoly objects
  """
  if type(other) == int:
   return self.scalarprod(other)
  
  if self.base != other.base:
   print('Cannot multiply %s, %s' %(self,other))
   return None
  x = self.coeffs
  y = other.coeffs
  nx = len(x)
  ny = len(y)
  base = self.base
  m = nx + ny
  zero = self.zero
  z = [zero for i in range(m)]
  for ix in range(nx):
   for iy in range(ny):
    z[ix+iy] += x[ix]*y[iy]
  return ZmodPoly(z,base,numclass=Zmod)

 def __eq__(self,other):
  if self.base != other.base:
   print('Cannot compare %s, %s' %(self,other))
   return None
  return (self.coeffs == other.coeffs)

 def lead(self):
  lead_coeff =  self.coeffs[-1]  # coefficient of highest term
  d = self.deg()
  # x^d
  coeffs = [0 for i in range(d+1)]
  #coeffs[-1] = lead_coeff
  return ZmodPoly(coeffs)

 def divmod(self,other):
  """ Division algorithm for polynomials
   a = self, b = other
   Divide a by b; 
   return q and r with
   a = b*q + r and either 
    q == zero and r = b OR
    deg(r) < deg(b)
  """
  dbg=False
  qlist = []
  a = self
  b = other
  da = a.deg()
  db = b.deg()
  base = a.base
  r = a
  zero = ZmodPoly.zero(base)
  q = zero
  for i in range(da+1):
   ans = ZmodPoly.divstep(r,b)
   #print('debug return after step')
   #return None
   if ans == None:
    return ans
   q1,r1 = ans
   if dbg:
    print('r = %s divide by b = %s\n  q1 = %s\n  r1 = %s' %(r,b,q1,r1))
    print()
   q = q + q1
   if ((r1 == zero) or (r1.deg() < db)):
    return(q,r1)
   else:
    r = r1 # continue divstep
  # loop ended without return
  print('ZmodPoly.divmod ERROR: loop fails to return')
  return None
   
 def pow(self,k):
  if (type(k) == int) and (0<=k):
   pass
  else:
   print('ZmodPoly.pow Error: invalid exponent: %s' % k)
   return None
  base = self.base
  x = ZmodPoly.one(base)
  for j in range(k):
   x = x * self
  return x

 def __pow__(self,k):
  return self.pow(k)
 
 def eval(self,a):
  p = self
  if (type(a) == Zmod) and (p.base == a.base):
   pass
  else:
   print('ZmodPoly.eval: incompatible bases: %s %s' %(p.base, a.base))
   return None
  base = p.base
  apow = Zmod.one(base)
  v = Zmod.zero(base)
  for c in p.coeffs:
   v = v + (c*apow)
   apow = apow*a
  return v

 def roots(self):
  ans = []
  p = self
  base = p.base
  zero = Zmod.zero(base)
  for a in Zmod.generate(base):
   v = self.eval(a)
   if v == zero:
    ans.append(a)
  return ans

  
def test1():
 a = ZmodPoly([1,2,1],7)
 b = ZmodPoly([1,1],7)
 a,b = ZmodPoly([10,2,3],7), ZmodPoly([4,2],7)
 
 print('test1. Divide %s by %s' %(a,b))
 c = a.divmod(b)
 print(c)
 #print('type of c = ',type(c))
 if c != None:
  q,r = c
  print('test1. q=%s, r=%s' %(q,r))
  ok = (a == (b*q + r))
  print('ok=',ok)
 
if __name__ == "__main__":
 test1()
 
 

