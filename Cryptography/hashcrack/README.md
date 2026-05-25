# hashcrack
**Category:** Cryptography
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2025
---
## Description
A company stored a secret message on a server which got breached due to the admin
using weakly hashed passwords. Can you gain access to the secret stored within
the server?
**Hints:**
- Understanding hashes is very crucial
- Can you identify the hash algorithm? Look carefully at the length and structure
  of each hash
- Tried using any hash cracking tools?
---
## Approach
The challenge connected to a remote server via netcat which presented three hashes
one at a time. Each hash had to be cracked before the server would reveal the next
one. I identified each hash type by looking at its length — 32 characters meant MD5,
40 characters meant SHA-1, and 64 characters meant SHA-256. I used CrackStation to
crack all three hashes instantly since they were all common weak passwords stored in
rainbow tables. After entering all three correct plaintext passwords into the server
the flag was revealed.
---
## Solution
### Step 1 - Connect to the server
```bash
nc verbal-sleep.picoctf.net 60855
```
Output: Server greeted and presented the first hash
### Step 2 - Identify and crack the first hash (MD5)
Hash: 482c811da5d5b4bc6d497ffa98491e38
Length: 32 characters = MD5 (128-bit)
1. Go to https://crackstation.net/
2. Paste the hash and click Crack Hashes
Output: password123
```bash
Enter the password for identified hash: password123
Correct! You've cracked the MD5 hash with no secret found! Flag is yet to be revealed!!
```
### Step 3 - Identify and crack the second hash (SHA-1)
Hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
Length: 40 characters = SHA-1 (160-bit)
1. Paste the hash into CrackStation
2. Click Crack Hashes
Output: letmein
```bash
Enter the password for the identified hash: letmein
Correct! You've cracked the SHA-1 hash with no secret found! Almost there!!
```
### Step 4 - Identify and crack the third hash (SHA-256)
Hash: 916e8c4f79b25028c9e467f1eb8eee6d6bbdff965f9928310ad30a8d88697745
Length: 64 characters = SHA-256 (256-bit)
1. Paste the hash into CrackStation
2. Click Crack Hashes
Output: qwerty098
```bash
Enter the password for the identified hash: qwerty098
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_36a1cf73}
```
---
## Tools Used
- nc (netcat) - connecting to the remote challenge server
- CrackStation (https://crackstation.net/) - cracking all three hashes using
  rainbow tables
---
## Flag
picoCTF{UseStr0nG_h@shEs_&PaSswDs!_36a1cf73}
---
## What I Learned
- Hash type can be identified just by counting the character length — 32 is MD5,
  40 is SHA-1, and 64 is SHA-256
- Common weak passwords like password123 and letmein are instantly crackable using
  rainbow table lookups on CrackStation
- MD5 and SHA-1 are considered broken and should never be used for password hashing
- Even SHA-256 is unsafe for passwords if no salt is added and the password is weak
- Always use bcrypt, argon2, or scrypt with a salt for storing passwords securely
