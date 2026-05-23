# Shared Secret
**Category:** Cryptography
**Difficulty:** Medium
**CTF:** picoCTF 2025
---
## Description
Can two parties share a secret without ever meeting?
**Hints:**
- Look at what gets written to the output files
- What happens when a private key leaks?
---
## Approach
The challenge provided source code and output files. The source code implemented a
Diffie-Hellman key exchange where two parties compute a shared secret using public
parameters. Reading through the source code I noticed that the private key b was
being written directly into the output file which completely breaks the security of
the exchange. With b leaked I could recompute the shared secret using the formula
shared = A^b mod p. The encryption was a simple XOR using only 1 byte derived from
the shared secret as shared % 256. I wrote a Python script to recompute the shared
secret, derive the XOR key, and decrypt the flag.
---
## Solution
### Step 1 - Download the files
wget the challenge files directly into Kali
Files received: source.py, output.txt
### Step 2 - Read the source code
```bash
cat source.py
```
Output: Source code revealed Diffie-Hellman key exchange implementation
Key observations:
- Diffie-Hellman parameters g, p, A are all public
- Private key b is mistakenly written to the output file
- Encryption is done with single-byte XOR: enc = [x ^ (shared % 256)]
### Step 3 - Extract the leaked values from the output file
```bash
cat output.txt
```
Output: All values including the private key b printed to terminal
The private key b should never appear here — this is the vulnerability.
### Step 4 - Write the Python solve script
```bash
nano solve.py
```
Paste the following content:
A = 771122236020803078829911570090382183223626843114693013412703353349864301811612864849857638111588507084769437566078749825291937213523446695097948166153379036322108656350710200734137906115055446496743841090323252143278700024424965369059879247648625799137192258413471893876530475007392243768366999108564494255853654467
p = 1653798930689987750372209240014380521131540183716217687164747711336243702962818359267822691525697642105558753651223568056089606926425342081267821725904109431430327153613733358950243154522848602494020618427146508586350079988809469424456886589329449769221123659126892760967096413248127035734431548987006011015808526671
b = 50208755224927679676889419914954638671317374186456176291867113154914631965864781394943324742496504879881629496602926264780376453359514342927328337421130216054068538364106054287057330330101487573397155782423600918457898629016565925736341979750081645208090049660478198625198845590319575618169699602518408794571532497
enc = bytes.fromhex("7a636965495e4c716e625579396978397e553a6e3b3f3c386f6f77")
shared = pow(A, b, p)
key = shared % 256
flag = bytes([x ^ key for x in enc])
print(flag.decode())
Save and exit with Ctrl+X then Y
### Step 5 - Run the script
```bash
python3 solve.py
```
Output: Flag printed directly in the terminal!
---
## Tools Used
- cat - reading the source code and output file to identify the vulnerability
- Python3 - recomputing the shared secret and decrypting the flag
- pow(A, b, p) - Python built-in modular exponentiation to compute the shared secret
---
## Flag
picoCTF{dh_s3cr3t_0d1562ee}
---
## What I Learned
- Diffie-Hellman is secure only as long as private keys stay private — leaking b
  completely breaks it
- Always audit what your program writes to output files, secrets should never
  appear there
- XOR encryption with a single byte is extremely weak regardless of how complex
  the key derivation is
- pow(A, b, p) in Python handles massive modular exponentiation efficiently in
  one line
- Even mathematically strong algorithms like Diffie-Hellman fail instantly when
  implementation is flawed
