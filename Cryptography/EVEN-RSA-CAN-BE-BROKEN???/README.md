# EVEN-RSA-CAN-BE-BROKEN???
**Category:** Cryptography
**Difficulty:** Medium
**Points:** 100
**CTF:** picoCTF 2025
---
## Description
This service provides you an encrypted flag. Can you decrypt it with just N and e?
**Hints:**
- Understanding RSA is very crucial
- Can you identify what is wrong with the modulus N?
- What happens to RSA when N is even?
---
## Approach
The challenge connected to a remote server via netcat which gave three values — N,
e, and a ciphertext. The title hinted that something was wrong with the RSA
implementation. The first thing I noticed was that N was an even number which is
impossible in normal RSA because N = p x q and both p and q are supposed to be odd
primes. An even N means one of the prime factors is 2. This completely breaks RSA
because p = 2 and q = N / 2 can be computed instantly without any complex
factorization. With p and q known I could calculate phi(N) = (p-1)(q-1) = q-1,
then derive the private key d using modular inverse of e, and finally decrypt the
ciphertext using m = c^d mod N. I wrote a Python script to automate the entire
decryption and ran it in a second terminal while keeping the netcat connection open.
---
## Solution
### Step 1 - Connect to the server
```bash
nc verbal-sleep.picoctf.net 59652
```
Output: Server returned N, e, and ciphertextNote: These values change every time you connect so keep this terminal open and
run the solve script in a second terminal with the fresh values.
### Step 2 - Spot the vulnerability
Look at the last digit of N — it ends in 8 which is even.
In RSA, N = p x q where both p and q must be odd primes.
An even N means one prime factor is 2 which makes N trivially factorable.
### Step 3 - Install pycryptodome
```bash
pip install pycryptodome
```
This library provides the long_to_bytes function needed to convert the decrypted
integer back into readable text.
### Step 4 - Write the Python solve script
```bash
nanofind_flag.py
```
Paste the following content with the values from your netcat connection:
```python
from Crypto.Util.number import long_to_bytes

N = 17537614138261784213928370696328752813986709042120259741743863531969271925248508130709263987579968737098825108090143054462035829031497144145084077726439478
e = 65537
c = 1862202474168637121872319135644317889384481444154089212360721245109801826108338981069221317033529716486407831083567338102494200390951480362472079543955817

# Step 1: Factor N — since N is even, one prime must be 2
p = 2
q = N // 2

# Step 2: Compute phi(N) = (p-1)(q-1) = 1 x (q-1) = q-1
phi = q - 1

# Step 3: Compute private key d as modular inverse of e
d = pow(e, -1, phi)

# Step 4: Decrypt ciphertext
m = pow(c, d, N)

# Step 5: Convert integer back to readable text
print(long_to_bytes(m).decode())
```
Save and exit with Ctrl+X then Y
### Step 5 - Run the script
```bash
python3 find_flag.py
```
Output: Flag printed directly in the terminal!
---
## Tools Used
- nc (netcat) - connecting to the remote challenge server to get N, e, and ciphertext
- Python3 - writing the RSA decryption script
- pycryptodome - providing the long_to_bytes function to decode the flag
- pow(e, -1, phi) - Python built-in modular inverse to compute the private key d
---
## Flag
picoCTF{tw0_1$_pr!m3df98b648}
---
## What I Learned
- RSA modulus N must always be odd because it is the product of two odd primes —
  an even N instantly reveals that p = 2
- When p = 2, phi(N) simplifies to just q-1 making the private key trivial to compute
- The title EVEN RSA CAN BE BROKEN was the direct hint — even N = broken RSA
- Always keep the netcat terminal open and run the solve script in a second terminal
  since the values change with every new connection
- Never write a custom RSA key generator — always use tested libraries like OpenSSL
  or pycryptodome which enforce proper prime generation
