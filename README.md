Random generate RSA quiz & solution write to standard output.

**RSA algorithm (short description):**

- RSA keys create by selecting two primes: p and q and p  ≠ q .

- Compute the product of the two primes : ```n  = p * q```

- Compute Euler's totient function of n : ```phi = (p-1) * (q-1)``` .

- Choose an encryption key is e.<br>
  Criterion : 1 < e < phi and gcd(e,phi) == 1

- Compute the decryption key is d : ```d = modinv(e,phi)```.<br>
  Criterion : 1 < d < phi and e*d ≡ 1 (mod phi) .

- Public key is the pair of numbers  : ```public_key = (n, e)```.

- Private key is the pair of numbers  : ```private_key = (n, d)```.

- For encryption : ```ciphertext = (message ** e) % n```. <br>
  Optimization :  ```ciphertext =  powmod(message,e,n)``` .<br>
  Criterion : 0<=ciphertext<n.

- For decryption : ```decrypted_message = (ciphertext ** d) % n```. <br>
  Optimization :   ```decrypted_message = powmod(message,e,n)``` .

- Criterion : These variables  non-negative integers.


**Output example:**

```
RSA quiz problem:
p = 457
q = 281
e = 173
message = 94082
n = ?
phi = ?
d = ?
private_key = ?
public_key = ?
ciphertext = ?
decrypted_message = ?

Solution :
p = 457
q = 281
n = p * q = 128417
phi = (p-1) * (q-1) = 127680
e = 173
d = modinv(e,phi) = modinv(173,127680) = ?
  modinv(a, m) = egcd(a, m)[1] % m
  modinv(173, 127680) = egcd(173, 127680)[1] % 127680
    g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
    egcd(173, 127680)
    egcd(127680 % 173, 173) = egcd(6, 173)
      g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
      egcd(6, 173)
      egcd(173 % 6, 6) = egcd(5, 6)
        g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
        egcd(5, 6)
        egcd(6 % 5, 5) = egcd(1, 5)
          g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
          egcd(1, 5)
          egcd(5 % 1, 1) = egcd(0, 1)
      egcd(0, 1) = (1, 0, 1)
          egcd(0, 1) = (g, y, x) = (1, 0, 1)
     egcd(a, b) = egcd(1, 5) = (g, x - (b // a) * y, y) = (1, 1, 0)
        egcd(1, 5) = (g, y, x) = (1, 1, 0)
    egcd(a, b) = egcd(5, 6) = (g, x - (b // a) * y, y) = (1, -1, 1)
      egcd(5, 6) = (g, y, x) = (1, -1, 1)
   egcd(a, b) = egcd(6, 173) = (g, x - (b // a) * y, y) = (1, 29, -1)
    egcd(6, 173) = (g, y, x) = (1, 29, -1)
  egcd(a, b) = egcd(173, 127680) = (g, x - (b // a) * y, y) = (1, -21403, 29)
  modinv(173, 127680) = -21403 % 127680 = 106277
d = modinv(e,phi) = modinv(173,127680) = 106277
public_key = (n, e) = (128417, 173)
private_key = (n, d) = (128417, 106277)
message = 94082
ciphertext = (message ** e) % n =  (94082 ** 173) % 128417 = powmod(94082,173,128417) = ?
  powmod(a,b,n) = powmod(94082,173,128417)
  e = a%n if b%2 == 1 else 1 ( = 94082 )
  a2 = a = 94082
  b>>=1  ( = 86 )
  a2 = (a2*a2) % n = (94082*94082) % 128417 = 24165
  b>>=1 ( = 43 )
  a2 = (a2*a2) % n = (24165*24165) % 128417 = 35126
  e = (e*a2) % n = (94082*35126) % 128417 = 41254
  b>>=1 ( = 21 )
  a2 = (a2*a2) % n = (35126*35126) % 128417 = 5340
  e = (e*a2) % n = (41254*5340) % 128417 = 61205
  b>>=1 ( = 10 )
  a2 = (a2*a2) % n = (5340*5340) % 128417 = 7026
  b>>=1 ( = 5 )
  a2 = (a2*a2) % n = (7026*7026) % 128417 = 52548
  e = (e*a2) % n = (61205*52548) % 128417 = 124992
  b>>=1 ( = 2 )
  a2 = (a2*a2) % n = (52548*52548) % 128417 = 69970
  b>>=1 ( = 1 )
  a2 = (a2*a2) % n = (69970*69970) % 128417 = 31192
  e = (e*a2) % n = (124992*31192) % 128417 = 10344
  b>>=1 ( = 0 )
  powmod(94082,173,128417) = 10344
ciphertext = (message ** e) % n =  (94082 ** 173) % 128417 = powmod(94082,173,128417) = 10344
decrypted_message = (ciphertext ** d) % n = (10344 ** 106277) % 128417 = powmod(10344,106277,128417) = ?
  powmod(a,b,n) = powmod(10344,106277,128417)
  e = a%n if b%2 == 1 else 1 ( = 10344 )
  a2 = a = 10344
  b>>=1  ( = 53138 )
  a2 = (a2*a2) % n = (10344*10344) % 128417 = 26975
  b>>=1 ( = 26569 )
  a2 = (a2*a2) % n = (26975*26975) % 128417 = 39903
  e = (e*a2) % n = (10344*39903) % 128417 = 24394
  b>>=1 ( = 13284 )
  a2 = (a2*a2) % n = (39903*39903) % 128417 = 7026
  b>>=1 ( = 6642 )
  a2 = (a2*a2) % n = (7026*7026) % 128417 = 52548
  b>>=1 ( = 3321 )
  a2 = (a2*a2) % n = (52548*52548) % 128417 = 69970
  e = (e*a2) % n = (24394*69970) % 128417 = 57833
  b>>=1 ( = 1660 )
  a2 = (a2*a2) % n = (69970*69970) % 128417 = 31192
  b>>=1 ( = 830 )
  a2 = (a2*a2) % n = (31192*31192) % 128417 = 53672
  b>>=1 ( = 415 )
  a2 = (a2*a2) % n = (53672*53672) % 128417 = 33440
  e = (e*a2) % n = (57833*33440) % 128417 = 103917
  b>>=1 ( = 207 )
  a2 = (a2*a2) % n = (33440*33440) % 128417 = 106781
  e = (e*a2) % n = (103917*106781) % 128417 = 105041
  b>>=1 ( = 103 )
  a2 = (a2*a2) % n = (106781*106781) % 128417 = 36531
  e = (e*a2) % n = (105041*36531) % 128417 = 24394
  b>>=1 ( = 51 )
  a2 = (a2*a2) % n = (36531*36531) % 128417 = 4497
  e = (e*a2) % n = (24394*4497) % 128417 = 31700
  b>>=1 ( = 25 )
  a2 = (a2*a2) % n = (4497*4497) % 128417 = 61540
  e = (e*a2) % n = (31700*61540) % 128417 = 35353
  b>>=1 ( = 12 )
  a2 = (a2*a2) % n = (61540*61540) % 128417 = 25853
  b>>=1 ( = 6 )
  a2 = (a2*a2) % n = (25853*25853) % 128417 = 95541
  b>>=1 ( = 3 )
  a2 = (a2*a2) % n = (95541*95541) % 128417 = 73904
  e = (e*a2) % n = (35353*73904) % 128417 = 84247
  b>>=1 ( = 1 )
  a2 = (a2*a2) % n = (73904*73904) % 128417 = 97789
  e = (e*a2) % n = (84247*97789) % 128417 = 94082
  b>>=1 ( = 0 )
  powmod(10344,106277,128417) = 94082
decrypted_message = (ciphertext ** d) % n = (10344 ** 106277) % 128417 = powmod(10344,106277,128417) = 94082
```
