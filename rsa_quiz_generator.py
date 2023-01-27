#!/usr/bin/env python3

import Crypto.Random.random, math,sys,io

class ModularInverseError(Exception):
    def __init__(self, message):            
        # Call the base class constructor with the parameters it needs
        super().__init__(message)            
        # Now for your custom code...
        #self.errors = errors

def powmod(a,b,n):
  global deep
  deep+=1
  s = f'powmod({a},{b},{n})'
  print((' '*(2*deep))+f'powmod(a,b,n) = {s}')
  e = a % n if b % 2 == 1 else 1
  print((' '*(2*deep))+f'e = a % n if b % 2 == 1 else 1  -->  e = {a} % {n} if {b} % 2 == 1 else 1  -->  e = {e}')
  a2 = a
  print((' '*(2*deep))+f'a2 = a  -->  a2 = {a2}')
  print(end=(' '*(2*deep))+f'b >>= 1  -->  b = {b} >> 1 = ')
  b >>= 1
  print(f"{b}")
  while b>0:
    print(end=(' '*(2*deep))+f'a2 = ( a2 * a2 ) % n  -->  a2 = ( {a2} * {a2} ) % {n} = ')
    a2 = ( a2 * a2 ) % n
    print(f'{a2}')
    if b % 2 == 1:
      print(end=(' '*(2*deep))+f'e = ( e * a2 ) % n  -->  e = ( {e} * {a2} ) % {n} = ')
      e = (e*a2) % n
      print(f'{e}')
    print(end=(' '*(2*deep))+f'b >>= 1  -->  b = {b} >> 1 = ')
    b >>= 1
    print(f"{b}")    
  print((' '*(2*deep))+f'{s} = {e}')
  deep-=1
  return e

#https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    global deep
    deep+=1
    s = f"egcd(a, b) = egcd({a}, {b})"
    print((' '*(2*deep))+s)
    x0, x1, y0, y1 = 0, 1, 1, 0
    print((' '*(2*deep))+f"x0, x1, y0, y1 = {x0}, {x1}, {y0}, {y1}")
    while a != 0:
        print(end=(' '*(2*deep))+f"(q, a), b = divmod(b, a), a  -->  (q, a), b = divmod({b}, {a}), {a}  -->  (q, a), b = ")
        (q, a), b = divmod(b, a), a
        print(f"({q}, {a}), {b}")
        print(end=(' '*(2*deep))+f"y0, y1 = y1, y0 - q * y1  -->  y0, y1 = {y1}, {y0} - {q} * {y1}  -->  ")
        y0, y1 = y1, y0 - q * y1
        print(f"y0, y1 = {y0}, {y1}")
        print(end=(' '*(2*deep))+f"x0, x1 = x1, x0 - q * x1  -->  x0, x1 = {x1}, {x0} - {q} * {x1}  -->  ")
        x0, x1 = x1, x0 - q * x1
        print(f"x0, x1 = {x0}, {x1}")
    print((' '*(2*deep))+f"{s} = (b, x0, y0) = ({b}, {x0}, {y0})")
    deep-=1
    return b, x0, y0

def modinv(a, m):
    global deep
    deep+=1
    print((' '*(2*deep))+'modinv(a, m) = egcd(a, m)[1] % m')
    print((' '*(2*deep))+f'modinv({a}, {m}) = egcd({a}, {m})[1] % {m}')
    g, x, y = egcd(a, m)
    if g != 1:
        raise ModularInverseError((' '*(2*deep))+f'modinv({a}, {m}) modular inverse does not exist')
    else:
        print((' '*(2*deep))+f'modinv({a}, {m}) = {x} % {m} = {x % m}')
        deep-=1
        return x % m

def sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def quiz_generate_raw(somePrimes , somePrimes2):
    global deep
    deep = 0
    p,q,e,message,n,phi,d,private_key,public_key,ciphertext,decrypted_message = 11 * [None]
    result = lambda success : (success,{'p':p , 'q':q ,'e':e , 'message':message ,  'n':n , 'phi':phi , 'd':d , 'private_key':private_key, 'public_key':public_key, 'ciphertext' : ciphertext, 'decrypted_message' : decrypted_message})
    # Choose two prime numbers, p and q
    p,q = Crypto.Random.random.sample(somePrimes,k=2)
    print(f'p = {p}\nq = {q}')
    # Compute n = pq
    n = p * q
    print(f'n = p * q = {n}')
    # Compute Euler's totient function of n
    phi = (p-1) * (q-1)
    print(f'phi = (p-1) * (q-1) = {phi}')
    # Choose an encryption key e, 1 < e < phi and gcd(e,phi) = 1
    while 1:      
      e = Crypto.Random.random.choice(
            somePrimes 
            if Crypto.Random.random.randrange(len(somePrimes)+len(somePrimes2))<len(somePrimes) else 
            somePrimes2
          )
      if 1 < e < phi and math.gcd(e,phi) == 1:
        break
    print(f'e = {e}')
    assert 1 < e < phi and math.gcd(e,phi) == 1
    # Compute the decryption key d, 1 < d < phi and e*d ≡ 1 (mod phi)
    try:
      print(f'd = modinv(e,phi) = modinv({e},{phi}) = ?')
      d = modinv(e,phi)
    except ModularInverseError as e:
      print(str(e))
      print(40*'-')
      return result(False)  
    print(f'd = modinv(e,phi) = modinv({e},{phi}) = {d}')
    # Public key (n,e)
    public_key = (n, e)
    print(f'public_key = (n, e) = {(n, e)}')
    # Private key (n,d)
    private_key = (n, d)
    print(f'private_key = (n, d) = {(n,d)}')
    # Message to encrypt
    message = Crypto.Random.random.randrange(n)
    print(f'message = {message}')
    # Encryption: ciphertext = message^e mod n
    print(f'ciphertext = (message ** e) % n =  ({message} ** {e}) % {n} = powmod({message},{e},{n}) = ?')
    ciphertext = powmod(message,e,n) #ciphertext = (message ** e) % n
    print(f'ciphertext = (message ** e) % n =  ({message} ** {e}) % {n} = powmod({message},{e},{n}) = {ciphertext}')
    # Decryption: message = ciphertext^d mod n
    print(f'decrypted_message = (ciphertext ** d) % n = ({ciphertext} ** {d}) % {n} = powmod({ciphertext},{d},{n}) = ?')
    decrypted_message = powmod(ciphertext,d,n)#decrypted_message = (ciphertext ** d) % n
    print(f'decrypted_message = (ciphertext ** d) % n = ({ciphertext} ** {d}) % {n} = powmod({ciphertext},{d},{n}) = {decrypted_message}')
    return result(True)

def quiz(p,q,e,message):
    print('RSA quiz problem:')
    print(f'p = {p}')
    print(f'q = {q}')
    print(f'e = {e}')
    print(f'message = {message}')
    print('n = ?')
    print('phi = ?')
    print('d = ?')
    print('private_key = ?')
    print('public_key = ?')
    print('ciphertext = ?')
    print('decrypted_message = ?')

def quiz_gen_and_solution(somePrimes , somePrimes2):
    stdout=sys.stdout
    sys.stdout = io.StringIO()
    succes, values = quiz_generate_raw(somePrimes , somePrimes2)
    assert succes 
    solved_str = sys.stdout.getvalue()
    sys.stdout = stdout
    quiz(values['p'],values['q'],values['e'],values['message'])
    print('\nSolution :\n'+solved_str)

def main():
  somePrimes = list(sieve(1000))
  somePrimes , somePrimes2 = somePrimes[23:] , somePrimes[:23]
  quiz_gen_and_solution(somePrimes , somePrimes2)
  
if __name__=='__main__':
  main()
