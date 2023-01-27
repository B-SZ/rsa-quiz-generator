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
p = 673
q = 191
e = 271
message = 32839
n = ?
phi = ?
d = ?
private_key = ?
public_key = ?
ciphertext = ?
decrypted_message = ?

Solution :
p = 673
q = 191
n = p * q = 128543
phi = (p-1) * (q-1) = 127680
e = 271
d = modinv(e,phi) = modinv(271,127680) = ?
  modinv(a, m) = egcd(a, m)[1] % m
  modinv(271, 127680) = egcd(271, 127680)[1] % 127680
    egcd(a, b) = egcd(271, 127680)
    x0, x1, y0, y1 = 0, 1, 1, 0
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(127680, 271), 271  -->  (q, a), b = (471, 39), 271
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 0, 1 - 471 * 0  -->  y0, y1 = 0, 1
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 1, 0 - 471 * 1  -->  x0, x1 = 1, -471
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(271, 39), 39  -->  (q, a), b = (6, 37), 39
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 1, 0 - 6 * 1  -->  y0, y1 = 1, -6
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = -471, 1 - 6 * -471  -->  x0, x1 = -471, 2827
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(39, 37), 37  -->  (q, a), b = (1, 2), 37
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = -6, 1 - 1 * -6  -->  y0, y1 = -6, 7
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 2827, -471 - 1 * 2827  -->  x0, x1 = 2827, -3298
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(37, 2), 2  -->  (q, a), b = (18, 1), 2
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = 7, -6 - 18 * 7  -->  y0, y1 = 7, -132
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = -3298, 2827 - 18 * -3298  -->  x0, x1 = -3298, 62191
    (q, a), b = divmod(b, a), a  -->  (q, a), b = divmod(2, 1), 1  -->  (q, a), b = (2, 0), 1
    y0, y1 = y1, y0 - q * y1  -->  y0, y1 = -132, 7 - 2 * -132  -->  y0, y1 = -132, 271
    x0, x1 = x1, x0 - q * x1  -->  x0, x1 = 62191, -3298 - 2 * 62191  -->  x0, x1 = 62191, -127680
    egcd(a, b) = egcd(271, 127680) = (b, x0, y0) = (1, 62191, -132)
  modinv(271, 127680) = 62191 % 127680 = 62191
d = modinv(e,phi) = modinv(271,127680) = 62191
public_key = (n, e) = (128543, 271)
private_key = (n, d) = (128543, 62191)
message = 32839
ciphertext = (message ** e) % n =  (32839 ** 271) % 128543 = powmod(32839,271,128543) = ?
  powmod(a,b,n) = powmod(32839,271,128543)
  e = a % n if b % 2 == 1 else 1  -->  e = 32839 % 128543 if 271 % 2 == 1 else 1  -->  e = 32839
  a2 = a  -->  a2 = 32839
  b >>= 1  -->  b = 271 >> 1 = 135
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 32839 * 32839 ) % 128543 = 52694
  e = ( e * a2 ) % n  -->  e = ( 32839 * 52694 ) % 128543 = 100943
  b >>= 1  -->  b = 135 >> 1 = 67
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 52694 * 52694 ) % 128543 = 293
  e = ( e * a2 ) % n  -->  e = ( 100943 * 293 ) % 128543 = 11409
  b >>= 1  -->  b = 67 >> 1 = 33
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 293 * 293 ) % 128543 = 85849
  e = ( e * a2 ) % n  -->  e = ( 11409 * 85849 ) % 128543 = 82124
  b >>= 1  -->  b = 33 >> 1 = 16
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 85849 * 85849 ) % 128543 = 37896
  b >>= 1  -->  b = 16 >> 1 = 8
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 37896 * 37896 ) % 128543 = 24420
  b >>= 1  -->  b = 8 >> 1 = 4
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 24420 * 24420 ) % 128543 = 25423
  b >>= 1  -->  b = 4 >> 1 = 2
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 25423 * 25423 ) % 128543 = 14725
  b >>= 1  -->  b = 2 >> 1 = 1
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 14725 * 14725 ) % 128543 = 102127
  e = ( e * a2 ) % n  -->  e = ( 82124 * 102127 ) % 128543 = 32627
  b >>= 1  -->  b = 1 >> 1 = 0
  powmod(32839,271,128543) = 32627
ciphertext = (message ** e) % n =  (32839 ** 271) % 128543 = powmod(32839,271,128543) = 32627
decrypted_message = (ciphertext ** d) % n = (32627 ** 62191) % 128543 = powmod(32627,62191,128543) = ?
  powmod(a,b,n) = powmod(32627,62191,128543)
  e = a % n if b % 2 == 1 else 1  -->  e = 32627 % 128543 if 62191 % 2 == 1 else 1  -->  e = 32627
  a2 = a  -->  a2 = 32627
  b >>= 1  -->  b = 62191 >> 1 = 31095
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 32627 * 32627 ) % 128543 = 56546
  e = ( e * a2 ) % n  -->  e = ( 32627 * 56546 ) % 128543 = 77206
  b >>= 1  -->  b = 31095 >> 1 = 15547
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 56546 * 56546 ) % 128543 = 71534
  e = ( e * a2 ) % n  -->  e = ( 77206 * 71534 ) % 128543 = 4009
  b >>= 1  -->  b = 15547 >> 1 = 7773
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 71534 * 71534 ) % 128543 = 73412
  e = ( e * a2 ) % n  -->  e = ( 4009 * 73412 ) % 128543 = 73781
  b >>= 1  -->  b = 7773 >> 1 = 3886
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 73412 * 73412 ) % 128543 = 27926
  b >>= 1  -->  b = 3886 >> 1 = 1943
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 27926 * 27926 ) % 128543 = 119638
  e = ( e * a2 ) % n  -->  e = ( 73781 * 119638 ) % 128543 = 92011
  b >>= 1  -->  b = 1943 >> 1 = 971
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 119638 * 119638 ) % 128543 = 116537
  e = ( e * a2 ) % n  -->  e = ( 92011 * 116537 ) % 128543 = 14476
  b >>= 1  -->  b = 971 >> 1 = 485
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 116537 * 116537 ) % 128543 = 47333
  e = ( e * a2 ) % n  -->  e = ( 14476 * 47333 ) % 128543 = 58318
  b >>= 1  -->  b = 485 >> 1 = 242
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 47333 * 47333 ) % 128543 = 36942
  b >>= 1  -->  b = 242 >> 1 = 121
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 36942 * 36942 ) % 128543 = 98876
  e = ( e * a2 ) % n  -->  e = ( 58318 * 98876 ) % 128543 = 68674
  b >>= 1  -->  b = 121 >> 1 = 60
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 98876 * 98876 ) % 128543 = 125511
  b >>= 1  -->  b = 60 >> 1 = 30
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 125511 * 125511 ) % 128543 = 66471
  b >>= 1  -->  b = 30 >> 1 = 15
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 66471 * 66471 ) % 128543 = 113845
  e = ( e * a2 ) % n  -->  e = ( 68674 * 113845 ) % 128543 = 77727
  b >>= 1  -->  b = 15 >> 1 = 7
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 113845 * 113845 ) % 128543 = 78964
  e = ( e * a2 ) % n  -->  e = ( 77727 * 78964 ) % 128543 = 92207
  b >>= 1  -->  b = 7 >> 1 = 3
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 78964 * 78964 ) % 128543 = 77995
  e = ( e * a2 ) % n  -->  e = ( 92207 * 77995 ) % 128543 = 89744
  b >>= 1  -->  b = 3 >> 1 = 1
  a2 = ( a2 * a2 ) % n  -->  a2 = ( 77995 * 77995 ) % 128543 = 51093
  e = ( e * a2 ) % n  -->  e = ( 89744 * 51093 ) % 128543 = 32839
  b >>= 1  -->  b = 1 >> 1 = 0
  powmod(32627,62191,128543) = 32839
decrypted_message = (ciphertext ** d) % n = (32627 ** 62191) % 128543 = powmod(32627,62191,128543) = 32839

```
