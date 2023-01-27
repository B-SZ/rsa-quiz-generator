Random generate RSA quiz & solution write to standard output.

**RSA algorithm (short description):**

- RSA keys create by selecting two primes: ```p``` , ```q``` and ```p ≠ q```.

- Compute the product of the two primes : ```n = p * q```

- Compute Euler's totient function of n : ```phi = (p-1) * (q-1)```.

- Choose an encryption key is ```e```.<br>
  Criterion : ```1 < e < phi and gcd(e,phi) == 1```.

- Compute the decryption key is ```d``` : ```d = modinv(e,phi)```.<br>
  Criterion : ```1 < d < phi and e*d ≡ 1 (mod phi)```.

- Public key is the pair of numbers  : ```public_key = (n, e)```.

- Private key is the pair of numbers  : ```private_key = (n, d)```.

- Message for encryption : ```ciphertext = (message ** e) % n```. <br>
  Optimization :  ```ciphertext =  powmod(message,e,n)``` .<br>
  Criterion : ```0 ≤ message < n```.

- Ciphertext for decryption : ```decrypted_message = (ciphertext ** d) % n```. <br>
  Optimization :   ```decrypted_message = powmod(message,e,n)```.

- Criterion : These variables  non-negative integers.


**Quiz & solution generated example:**

```
RSA quiz problem:
p = 181
q = 367
e = 167
message = 7800
n = ?
phi = ?
d = ?
private_key = ?
public_key = ?
ciphertext = ?
decrypted_message = ?

Solution :
p = 181
q = 367
n = p * q = 66427
phi = (p-1) * (q-1) = 65880
e = 167
d = modinv(e,phi) = modinv(167,65880) = ?
  modinv(a, m) = egcd(a, m)[1] % m
  modinv(167, 65880) = egcd(167, 65880)[1] % 65880
    g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
    egcd(167, 65880)
    egcd(65880 % 167, 167) = egcd(82, 167)
      g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
      egcd(82, 167)
      egcd(167 % 82, 82) = egcd(3, 82)
        g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
        egcd(3, 82)
        egcd(82 % 3, 3) = egcd(1, 3)
          g, y, x = egcd(b % a, a) ; egcd(a, b) = (g, x - (b // a) * y, y)
          egcd(1, 3)
          egcd(3 % 1, 1) = egcd(0, 1)
            egcd(0, 1) = (1, 0, 1)
          egcd(0, 1) = (g, y, x) = (1, 0, 1)
          egcd(a, b) = egcd(1, 3) = (g, x - (b // a) * y, y) = (1, 1, 0)
        egcd(1, 3) = (g, y, x) = (1, 1, 0)
        egcd(a, b) = egcd(3, 82) = (g, x - (b // a) * y, y) = (1, -27, 1)
      egcd(3, 82) = (g, y, x) = (1, -27, 1)
      egcd(a, b) = egcd(82, 167) = (g, x - (b // a) * y, y) = (1, 55, -27)
    egcd(82, 167) = (g, y, x) = (1, 55, -27)
    egcd(a, b) = egcd(167, 65880) = (g, x - (b // a) * y, y) = (1, -21697, 55)
  modinv(167, 65880) = -21697 % 65880 = 44183
d = modinv(e,phi) = modinv(167,65880) = 44183
public_key = (n, e) = (66427, 167)
private_key = (n, d) = (66427, 44183)
message = 7800
ciphertext = (message ** e) % n =  (7800 ** 167) % 66427 = powmod(7800,167,66427) = ?
  powmod(a,b,n) = powmod(7800,167,66427)
  e = a%n if b%2 == 1 else 1 ( = 7800 )
  a2 = a = 7800
  b>>=1  ( = 83 )
  a2 = (a2*a2) % n = (7800*7800) % 66427 = 59295
  e = (e*a2) % n = (7800*59295) % 66427 = 36226
  b>>=1 ( = 41 )
  a2 = (a2*a2) % n = (59295*59295) % 66427 = 48769
  e = (e*a2) % n = (36226*48769) % 66427 = 13302
  b>>=1 ( = 20 )
  a2 = (a2*a2) % n = (48769*48769) % 66427 = 63053
  b>>=1 ( = 10 )
  a2 = (a2*a2) % n = (63053*63053) % 66427 = 24859
  b>>=1 ( = 5 )
  a2 = (a2*a2) % n = (24859*24859) % 66427 = 65927
  e = (e*a2) % n = (13302*65927) % 66427 = 58127
  b>>=1 ( = 2 )
  a2 = (a2*a2) % n = (65927*65927) % 66427 = 50719
  b>>=1 ( = 1 )
  a2 = (a2*a2) % n = (50719*50719) % 66427 = 31386
  e = (e*a2) % n = (58127*31386) % 66427 = 22894
  b>>=1 ( = 0 )
  powmod(7800,167,66427) = 22894
ciphertext = (message ** e) % n =  (7800 ** 167) % 66427 = powmod(7800,167,66427) = 22894
decrypted_message = (ciphertext ** d) % n = (22894 ** 44183) % 66427 = powmod(22894,44183,66427) = ?
  powmod(a,b,n) = powmod(22894,44183,66427)
  e = a%n if b%2 == 1 else 1 ( = 22894 )
  a2 = a = 22894
  b>>=1  ( = 22091 )
  a2 = (a2*a2) % n = (22894*22894) % 66427 = 26206
  e = (e*a2) % n = (22894*26206) % 66427 = 57927
  b>>=1 ( = 11045 )
  a2 = (a2*a2) % n = (26206*26206) % 66427 = 32110
  e = (e*a2) % n = (57927*32110) % 66427 = 13543
  b>>=1 ( = 5522 )
  a2 = (a2*a2) % n = (32110*32110) % 66427 = 38633
  b>>=1 ( = 2761 )
  a2 = (a2*a2) % n = (38633*38633) % 66427 = 26853
  e = (e*a2) % n = (13543*26853) % 66427 = 48781
  b>>=1 ( = 1380 )
  a2 = (a2*a2) % n = (26853*26853) % 66427 = 18524
  b>>=1 ( = 690 )
  a2 = (a2*a2) % n = (18524*18524) % 66427 = 43121
  b>>=1 ( = 345 )
  a2 = (a2*a2) % n = (43121*43121) % 66427 = 62484
  e = (e*a2) % n = (48781*62484) % 66427 = 29109
  b>>=1 ( = 172 )
  a2 = (a2*a2) % n = (62484*62484) % 66427 = 3331
  b>>=1 ( = 86 )
  a2 = (a2*a2) % n = (3331*3331) % 66427 = 2252
  b>>=1 ( = 43 )
  a2 = (a2*a2) % n = (2252*2252) % 66427 = 23052
  e = (e*a2) % n = (29109*23052) % 66427 = 41541
  b>>=1 ( = 21 )
  a2 = (a2*a2) % n = (23052*23052) % 66427 = 45131
  e = (e*a2) % n = (41541*45131) % 66427 = 17650
  b>>=1 ( = 10 )
  a2 = (a2*a2) % n = (45131*45131) % 66427 = 22487
  b>>=1 ( = 5 )
  a2 = (a2*a2) % n = (22487*22487) % 66427 = 22845
  e = (e*a2) % n = (17650*22845) % 66427 = 2360
  b>>=1 ( = 2 )
  a2 = (a2*a2) % n = (22845*22845) % 66427 = 43513
  b>>=1 ( = 1 )
  a2 = (a2*a2) % n = (43513*43513) % 66427 = 12388
  e = (e*a2) % n = (2360*12388) % 66427 = 7800
  b>>=1 ( = 0 )
  powmod(22894,44183,66427) = 7800
decrypted_message = (ciphertext ** d) % n = (22894 ** 44183) % 66427 = powmod(22894,44183,66427) = 7800
```
