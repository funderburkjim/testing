
class Z7(object):
 base = 7
 zeroparm = 0
 oneparm = 1
 
 @classmethod
 def normalize(cls,n):
  q,r = divmod(n,cls.base)
  return r
 @classmethod
 def mult_inverse(cls,n):
  from numtheory1 import Nmod_inverse
  a = Nmod_inverse(n,cls.base)
  if a == None:
   print('%s has no multiplicative inverse modulo %s' %(n,cls.base))
   return 0  # questionable. Maybe should raise exception
  ans,r = a  # r == 1
  return ans

 def __init__(self,n):
  # n assumed an int (Integer, positive or negative)
  self.n = self.normalize(n)
  c = self.__class__ # class constructor
  
 def __sum__(self,other):
  """ implement binary '+' 
  """
  x = self.n
  y = other.n
  z = self.normalize(x+y)
  c = self.__class__ # class constructor
  return c(z)
 
 def __sub__(self,other):
  """ implement binary '-' 
  """
  x = self.p
  y = other.p
  z = self.normalize(x+y)
  c = self.__class__ # class constructor
  return c(z)
 def __neg__(self):
  """ unary '-' for Poly objects
  """
  x = self.p
  z = self.normalize(-x)
  c = self.__class__ # class constructor
  return c(z)
 def __mul__(self,other):
  """ implement binary '*' 
  """
  x = self.n
  y = other.n
  z = self.normalize(x*y)
  c = self.__class__ # class constructor
  return c(z)
 def __eq__(self,other):
  """ implement binary ==
  """
  return (self.p == other.p)
 
 def __truediv__(self,other):
  """ implement binary division /
   a*u = b (mod m)
   u = b*v (mod m) where v = b/a
  """
  x = self.n
  y = other.n
  y1 = self.mult_inverse(y)
  z = x*y1
  c = self.__class__ # class constructor
  return c(z)

     
