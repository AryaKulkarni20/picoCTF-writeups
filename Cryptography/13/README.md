# 13
**Category:** Cryptography
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2019
---
## Description
Cryptography can be easy, do you know what ROT13 is?
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
**Hints:**
- This can be solved online if you don't want to do it by hand!
---
## Approach
The challenge gave a ciphertext directly in the description with no files to
download. The challenge name 13 and the description directly mentioning ROT13
were both dead giveaways. ROT13 is a Caesar cipher with a fixed shift of 13 —
it works because the English alphabet has 26 letters so shifting by 13 twice
brings you back to the start making it both the encryption and decryption
function. I recognised cvpbPGS as picoCTF shifted by 13 which confirmed ROT13.
I used dCode Caesar cipher decoder to decode the ciphertext which revealed the
flag instantly.
---
## Solution
### Step 1 - Read the ciphertext from the challenge description
Ciphertext given directly on the challenge page:
cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}
### Step 2 - Identify the cipher
The challenge name is 13 — a direct reference to ROT13.
The description directly asks if you know what ROT13 is.
cvpbPGS maps exactly to picoCTF when each letter is shifted by 13 — confirmed ROT13.
### Step 3 - Decode using dCode Caesar Cipher
1. Open dCode Caesar cipher at https://www.dcode.fr/caesar-cipher
2. Paste cvpbPGS{abg_gbb_onq_bs_n_ceboyrz} into the input
3. Click Decrypt / Crack and let dCode brute force all 26 shifts
4. Look for the output starting with picoCTF
Output: Shift 13 (ROT13) reveals the flag
---
## Tools Used
- dCode Caesar Cipher (https://www.dcode.fr/caesar-cipher) - brute forcing all
  26 shifts to decode the ROT13 ciphertext and reveal the flag
---
## Flag
picoCTF{not_too_bad_of_a_problem}
---
## What I Learned
- The challenge name 13 is itself the hint — it directly points to ROT13
- ROT13 is a Caesar cipher with a fixed shift of 13 and is the most commonly
  seen rotation cipher in beginner CTF challenges
- cvpbPGS matching the length and structure of picoCTF is always the instant
  giveaway that ROT13 is being used
- ROT13 applied twice returns the original text making it both the encryption
  and decryption function since 13 + 13 = 26
- dCode Caesar cipher brute forces all 26 shifts instantly and highlights the
  correct decryption without any manual guessing
