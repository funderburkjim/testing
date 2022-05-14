"""
poly.py
a simple implementation of polynomials
The coefficients are assumed to be Python number objects.
Assume 0 is the additive identify for the numbers

"""

class Poly(object):
 def __init__(self,numlist):
  """numlist is a (non-empty) sequence of 'numbers'
  """
  self.p = list(numlist)
  self.normalize()
 def deg(self):
  """ degree of Poly object
  """
  d = 0 # the degree
  for i,a in enumerate(self.p):
   if a != 0:
    d = i
  return d

 def normalize(self):
  d = self.deg()
  self.p = self.p[0:d+1]

 def __sum__(self,other):
  """ implement binary '+' for Poly objects
  """
  x = self.p
  y = other.p
  nx = len(x)
  ny = len(y)
  m = max(nx,ny)
  z = []
  for i in range(m):
   # use ternary operator
   a = x[i] if (i < nx) else 0
   b = y[i] if (i < ny) else 0
   z.append(a+b)
  return Poly(z)

 def __sub__(self,other):
  """ implement binary '-' for Poly objects
  """
  x = self.p
  y = other.p
  nx = len(x)
  ny = len(y)
  m = max(nx,ny)
  z = []
  for i in range(m):
   # use ternary operator
   a = x[i] if (i < nx) else 0
   b = y[i] if (i < ny) else 0
   z.append(a-b)
  return Poly(z)

 def __neg__(self):
  """ unary '-' for Poly objects
  """
  x = self.p
  nx = len(x)
  z = []
  for i in range(nx):
   # use ternary operator
   a = x[i]
   z.append(-a)
  return Poly(z)

 def __mul__(self,other):
  x = self.p
  y = other.p
  nx = len(x)
  ny = len(y)
  m = nx + ny
  z = [0 for i in range(m)]
  for ix in range(nx):
   for iy in range(ny):
    z[ix+iy] += x[ix]*y[iy]
  return Poly(z)

 def __eq__(self,other):
  return (self.p == other.p)

 def lead(self):
  lead_coeff =  self.p[-1]  # coefficient of highest term
  d = self.deg()
  # x^d
  coeffs = [0 for i in range(d+1)]
  #coeffs[-1] = lead_coeff
  return Poly(coeffs)

 def __div__(self,d):
  # requires numbers to be in a field!
  # INCOMPLETE
  n = self
  zero = Poly[0]
  q = Poly[0]
  r = n
  # At each step n = d x q + 4
  while (r != zero) and (r.deg() >= d.deg()):
   # t = a*X^i / b*X^j = (a/b)*X^(i-j)
   # 
   #t = r.lead() / d.lead()
   #rlead = r.lead()
   #dlead = d.lead()
   rlc = r.p[-1] # highest non-zero coefficient
   rdeg = r.deg()
   dlc = d.p[-1]
   ddeg = d.deg()
   
 def __divx__(self,other):
  # def div(p,q):
  zero = [0]
  p = self.p
  q = other.p
  if q==[0]:
   return(None)
  else:
   l=[0]
   r=p
   while r!=[0] and q.degree()<=r.degree():
    t= r.leading_coefficient()/ q.leading_coefficient()
    m=x^r.degree()/x^q.degree()
    m=R(m)
    l=l+t*m
    r=r-(t*m*q)
    print(l,r)
   return(l,r)  
  

