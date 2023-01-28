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
p = 193
q = 89
e = 983
message = 14942
n = ?
phi = ?
d = ?
private_key = ?
public_key = ?
ciphertext = ?
decrypted_message = ?

Solution :
p = 193
q = 89
n = p * q = 17177
phi = (p-1) * (q-1) = 16896
e = 983
d = modinv(e,phi) = modinv(983,16896) = ?
  modinv(a, m) = egcd(a, m)[1] % m
  modinv(983, 16896) = egcd(983, 16896)[1] % 16896
    egcd(a, b) = egcd(983, 16896)
    x0, x1, y0, y1 = 0, 1, 1, 0
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(16896, 983), 983  -->  (q, a), b = (17, 185), 983
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 0, 1 - 17 * 0  -->  y0, y1 = 0, 1
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 1, 0 - 17 * 1  -->  x0, x1 = 1, -17
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(983, 185), 185  -->  (q, a), b = (5, 58), 185
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 1, 0 - 5 * 1  -->  y0, y1 = 1, -5
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = -17, 1 - 5 * -17  -->  x0, x1 = -17, 86
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(185, 58), 58  -->  (q, a), b = (3, 11), 58
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = -5, 1 - 3 * -5  -->  y0, y1 = -5, 16
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 86, -17 - 3 * 86  -->  x0, x1 = 86, -275
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(58, 11), 11  -->  (q, a), b = (5, 3), 11
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 16, -5 - 5 * 16  -->  y0, y1 = 16, -85
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = -275, 86 - 5 * -275  -->  x0, x1 = -275, 1461
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(11, 3), 3  -->  (q, a), b = (3, 2), 3
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = -85, 16 - 3 * -85  -->  y0, y1 = -85, 271
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 1461, -275 - 3 * 1461  -->  x0, x1 = 1461, -4658
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(3, 2), 2  -->  (q, a), b = (1, 1), 2
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 271, -85 - 1 * 271  -->  y0, y1 = 271, -356
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = -4658, 1461 - 1 * -4658  -->  x0, x1 = -4658, 6119
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(2, 1), 1  -->  (q, a), b = (2, 0), 1
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = -356, 271 - 2 * -356  -->  y0, y1 = -356, 983
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 6119, -4658 - 2 * 6119  -->  x0, x1 = 6119, -16896
    egcd(983, 16896) = (b, x0, y0) = (1, 6119, -356)
  modinv(983, 16896) = egcd(983, 16896)[1] % 16896 = 6119 % 16896 = 6119
d = modinv(e,phi) = modinv(983,16896) = 6119
public_key = (n, e) = (17177, 983)
private_key = (n, d) = (17177, 6119)
message = 14942
ciphertext = (message ** e) % n =  (14942 ** 983) % 17177 = powmod(14942,983,17177) = ?
  powmod(a,b,n) = powmod(14942,983,17177)
  e = a % n if b % 2 == 1 else 1  -->  e = 14942 % 17177 if 983 % 2 == 1 else 1  -->  e = 14942
  a2 = a  -->  a2 = 14942
  b >>= 1  -->  b = 983 >> 1 = 491
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 14942 * 14942 ) % 17177 = 13895
  e = ( e * a2 ) % n  -->  e = ( 14942 * 13895 ) % 17177 = 691
  b >>= 1  -->  b = 491 >> 1 = 245
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 13895 * 13895 ) % 17177 = 1545
  e = ( e * a2 ) % n  -->  e = ( 691 * 1545 ) % 17177 = 2621
  b >>= 1  -->  b = 245 >> 1 = 122
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 1545 * 1545 ) % 17177 = 16599
  b >>= 1  -->  b = 122 >> 1 = 61
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 16599 * 16599 ) % 17177 = 7721
  e = ( e * a2 ) % n  -->  e = ( 2621 * 7721 ) % 17177 = 2235
  b >>= 1  -->  b = 61 >> 1 = 30
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 7721 * 7721 ) % 17177 = 9651
  b >>= 1  -->  b = 30 >> 1 = 15
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 9651 * 9651 ) % 17177 = 8107
  e = ( e * a2 ) % n  -->  e = ( 2235 * 8107 ) % 17177 = 14587
  b >>= 1  -->  b = 15 >> 1 = 7
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 8107 * 8107 ) % 17177 = 4247
  e = ( e * a2 ) % n  -->  e = ( 14587 * 4247 ) % 17177 = 10727
  b >>= 1  -->  b = 7 >> 1 = 3
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 4247 * 4247 ) % 17177 = 1159
  e = ( e * a2 ) % n  -->  e = ( 10727 * 1159 ) % 17177 = 13622
  b >>= 1  -->  b = 3 >> 1 = 1
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 1159 * 1159 ) % 17177 = 3475
  e = ( e * a2 ) % n  -->  e = ( 13622 * 3475 ) % 17177 = 13815
  b >>= 1  -->  b = 1 >> 1 = 0
  powmod(14942,983,17177) = 13815
ciphertext = (message ** e) % n =  (14942 ** 983) % 17177 = powmod(14942,983,17177) = 13815
decrypted_message = (ciphertext ** d) % n = (13815 ** 6119) % 17177 = powmod(13815,6119,17177) = ?
  powmod(a,b,n) = powmod(13815,6119,17177)
  e = a % n if b % 2 == 1 else 1  -->  e = 13815 % 17177 if 6119 % 2 == 1 else 1  -->  e = 13815
  a2 = a  -->  a2 = 13815
  b >>= 1  -->  b = 6119 >> 1 = 3059
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 13815 * 13815 ) % 17177 = 578
  e = ( e * a2 ) % n  -->  e = ( 13815 * 578 ) % 17177 = 14942
  b >>= 1  -->  b = 3059 >> 1 = 1529
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 578 * 578 ) % 17177 = 7721
  e = ( e * a2 ) % n  -->  e = ( 14942 * 7721 ) % 17177 = 6450
  b >>= 1  -->  b = 1529 >> 1 = 764
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 7721 * 7721 ) % 17177 = 9651
  b >>= 1  -->  b = 764 >> 1 = 382
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 9651 * 9651 ) % 17177 = 8107
  b >>= 1  -->  b = 382 >> 1 = 191
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 8107 * 8107 ) % 17177 = 4247
  e = ( e * a2 ) % n  -->  e = ( 6450 * 4247 ) % 17177 = 13012
  b >>= 1  -->  b = 191 >> 1 = 95
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 4247 * 4247 ) % 17177 = 1159
  e = ( e * a2 ) % n  -->  e = ( 13012 * 1159 ) % 17177 = 16679
  b >>= 1  -->  b = 95 >> 1 = 47
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 1159 * 1159 ) % 17177 = 3475
  e = ( e * a2 ) % n  -->  e = ( 16679 * 3475 ) % 17177 = 4327
  b >>= 1  -->  b = 47 >> 1 = 23
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 3475 * 3475 ) % 17177 = 194
  e = ( e * a2 ) % n  -->  e = ( 4327 * 194 ) % 17177 = 14942
  b >>= 1  -->  b = 23 >> 1 = 11
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 194 * 194 ) % 17177 = 3282
  e = ( e * a2 ) % n  -->  e = ( 14942 * 3282 ) % 17177 = 16486
  b >>= 1  -->  b = 11 >> 1 = 5
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 3282 * 3282 ) % 17177 = 1545
  e = ( e * a2 ) % n  -->  e = ( 16486 * 1545 ) % 17177 = 14556
  b >>= 1  -->  b = 5 >> 1 = 2
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 1545 * 1545 ) % 17177 = 16599
  b >>= 1  -->  b = 2 >> 1 = 1
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 16599 * 16599 ) % 17177 = 7721
  e = ( e * a2 ) % n  -->  e = ( 14556 * 7721 ) % 17177 = 14942
  b >>= 1  -->  b = 1 >> 1 = 0
  powmod(13815,6119,17177) = 14942
decrypted_message = (ciphertext ** d) % n = (13815 ** 6119) % 17177 = powmod(13815,6119,17177) = 14942

```
