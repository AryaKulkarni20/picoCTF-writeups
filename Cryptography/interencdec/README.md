# interencdec
**Category:** Cryptography
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2024
---
## Description
Can you get the real meaning from this file?
**Hints:**
- Engaging in various decoding processes is of utmost importance
---
## Approach
The challenge gave a single file called enc_flag. I used the cat command to read
the file which showed a long string ending in == which is the classic indicator of
Base64 encoding. I decoded it using CyberChef with the From Base64 recipe which
gave another Base64 string wrapped inside b' ' — a Python byte literal format. I
stripped the b' ' wrapper and decoded the inner Base64 string again in CyberChef
which gave a flag-shaped string in the format wpjvJAM{...}. This looked exactly
like picoCTF{} but with all the letters shifted. I recognised this as a Caesar
cipher and used dCode to try all 26 shifts. Shift 19 (ROT19) revealed the final
flag starting with picoCTF.
---
## Solution
### Step 1 - Download the file
```bash
wget https://artifacts.picoctf.net/c_titan/3/enc_flag
```
File received: enc_flag
### Step 2 - Read the file
```bash
cat enc_flag
```
Output:
YidkM0JxZGtwQlRYdHFhR3g2YUhsZmF6TnFlVGwzWVROclgya3lNRFJvYTJvMmZRPT0nCg==
The == at the end confirms this is a Base64 encoded string.
### Step 3 - First Base64 decode using CyberChef
1. Open CyberChef at https://gchq.github.io/CyberChef/
2. Paste the string into the input
3. Use the From Base64 recipe
Output:
b'd3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2kyMDRoa2o2fQ=='
Still Base64 — the b' ' wrapper is a Python byte literal. Strip it and decode again.
### Step 4 - Second Base64 decode using CyberChef
1. Copy the string inside the b' ' quotes (without b' and ')
2. Paste it back into CyberChef
3. Use the From Base64 recipe again
Output:
wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6}
This looks exactly like picoCTF{} format but with letters shifted — Caesar cipher.
### Step 5 - Decode the Caesar cipher using dCode
1. Open dCode Caesar cipher at https://www.dcode.fr/caesar-cipher
2. Paste wpjvJAM{jhlzhy_k3jy9wa3k_i204hkj6} into the input
3. Click Decrypt / Crack and let dCode brute force all 26 shifts
4. Look for the output starting with picoCTF
Output: Shift 19 (ROT19) reveals the flag
---
## Tools Used
- cat - reading the enc_flag file contents
- CyberChef (https://gchq.github.io/CyberChef/) - decoding both layers of
  Base64 encoding using the From Base64 recipe
- dCode Caesar Cipher (https://www.dcode.fr/caesar-cipher) - brute forcing
  all 26 shifts to crack the Caesar cipher
---
## Flag
picoCTF{caesar_d3cr9pt3d_78250afc}
---
## What I Learned
- A string ending in == is almost always Base64 encoded — always try From Base64
  in CyberChef first
- Data can be encoded in multiple layers — always check if the decoded output is
  still encoded
- The b' ' wrapper is a Python byte literal and is not part of the actual encoded
  string — always strip it before decoding again
- wpjvJAM matching the length and capitalisation of picoCTF is the giveaway for
  a Caesar cipher
- dCode Caesar cipher brute forces all 26 shifts instantly and highlights the
  correct decryption without any manual guessing
