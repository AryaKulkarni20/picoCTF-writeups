# Mod 26
**Category:** Cryptography
**Difficulty:** Easy
**Points:** 10
**CTF:** picoCTF 2021
---
## Description
Cryptography can be easy, do you know what ROT13 is?
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}
**Hints:**
- This can be solved online if you don't want to do it by hand!
---
## Approach
The challenge gave a ciphertext directly in the description with no files to
download. The title Mod 26 and the description mentioning ROT13 were both direct
hints. ROT13 is a Caesar cipher with a fixed shift of 13 — it works because the
English alphabet has 26 letters so shifting by 13 twice brings you back to the
start making it its own inverse. I recognised cvpbPGS as picoCTF shifted by 13
which confirmed the cipher. I used dCode Caesar cipher decoder to decode the
ciphertext by setting the shift to 13 which revealed the flag instantly.
---
## Solution
### Step 1 - Read the ciphertext from the challenge description
Ciphertext given directly on the challenge page:
cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj}
### Step 2 - Identify the cipher
The title says Mod 26 — the alphabet has 26 letters.
The description directly mentions ROT13.
cvpbPGS maps exactly to picoCTF when each letter is shifted by 13 — confirmed ROT13.
### Step 3 - Decode using dCode Caesar Cipher
1. Open dCode Caesar cipher at https://www.dcode.fr/caesar-cipher
2. Paste cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_MAZyqFQj} into the input
3. Click Decrypt / Crack and let dCode brute force all 26 shifts
4. Look for the output starting with picoCTF
Output: Shift 13 (ROT13) reveals the flag
---
## Tools Used
- dCode Caesar Cipher (https://www.dcode.fr/caesar-cipher) - brute forcing all
  26 shifts to decode the ROT13 ciphertext and reveal the flag
---
## Flag
picoCTF{next_time_I'll_try_2_rounds_of_rot13_ZNMldSDw}
---
## What I Learned
- ROT13 is a Caesar cipher with a fixed shift of 13 — the most common rotation
  cipher seen in beginner CTF challenges
- The title Mod 26 was the hint — 26 letters in the alphabet, shift by 13 which
  is exactly half of 26
- dCode Caesar cipher brute forces all 26 shifts instantly and highlights the
  correct decryption without any manual guessing
- cvpbPGS matching the length and structure of picoCTF is always the giveaway
  that ROT13 is being used
- ROT13 applied twice returns the original text making it both the encryption
  and decryption function
