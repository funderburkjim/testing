import sys

def burton_qr_info():
 info = """
Ref: David M. Burton, Elementary NUmber Theory, 1976, p. 204-205.
Check a certain 'counting' method used in Burton's proof of 
Gauss quadratic reciprocity theorem.
Usage:  burton_qr(a,b)
  a,b should be odd relatively prime positive integers.
  To show ((a-1)/2)*((b-1)/2) = A + B, where
  A = Sum(k=1 to (a-1)/2 of Quo(kb,a))
  B = Sum(j=1 to (b-1)/2 of Quo(ka,b))

 """
 print(info)

def burton_qr_quosum(m,a,b):
 ans = 0
 indexes = range(1,m+1) # 1,...,m
 for k in indexes:
  q,r = divmod(k*b,a)
  ans = ans + q
 return ans

def burton_qr(a,b):
 a2,a2r = divmod(a,2)
 if a2r != 1:
  print("Expected first parameter to be odd positive integer")
 b2,b2r = divmod(b,2)
 if b2r != 1:
  print("Expected second parameter to be odd positive integer")
 A = burton_qr_quosum(a2,a,b)
 B = burton_qr_quosum(b2,b,a)
 print(a2*b2)
 print(A+B)

"""
Eisenstein's Lemma
Ref: https://en.wikipedia.org/wiki/Proofs_of_quadratic_reciprocity
This is similar to the burton approach

"""
def EisenLemma(a,p):
 # gcd(a,p) = 1
 # p an odd prime
 ans1 = []
 ans2 = []
 for k in range(2,p,2): # even positive numbers < p
  r = (k*a) % p # Rem(k*a,p)
  if (r % 2) == 0:
   r1 = r
  else:
   r1 = p - r
  ans1.append(r)
  ans2.append(r1)
 return ans1,ans2

if __name__ == "__main__":
 if len(sys.argv) != 3:
  print(sys.argv)
  burton_qr_info()
  print("xxx")
  exit(1)
 a = sys.argv[1]
 b = sys.argv[2]
 burton_qr(int(a),int(b))
