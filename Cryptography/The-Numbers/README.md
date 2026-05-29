# The Numbers
**Category:** Cryptography
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2019
---
## Description
The numbers... what do they mean?
**Hints:**
- The flag is in the format PICOCTF{}
---
## Approach
The challenge gave a single PNG image called the_numbers.png. Opening the image
revealed a sequence of numbers separated by spaces with curly braces around part
of them — clearly in the flag format PICOCTF{}. The hint confirmed the flag format
was uppercase. I noticed the first seven numbers were 16 9 3 15 3 20 6 and since
P is the 16th letter, I is the 9th, C is the 3rd and so on — this was a simple
A1Z26 cipher where each number represents the position of a letter in the alphabet.
I used Boxentriq numbers to letters decoder to convert all the numbers to letters
instantly which revealed the complete flag.
---
## Solution
### Step 1 - Download the file
```bash
wget https://artifacts.picoctf.net/c/55/the_numbers.png
```
File received: the_numbers.png
### Step 2 - Open the image
```bash
eog the_numbers.png
```
Output: Image displayed the following number sequence:
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
### Step 3 - Identify the cipher
The numbers all fall between 1 and 26 — the exact range of the English alphabet.
The hint says the flag format is PICOCTF{} in uppercase.
16 = P, 9 = I, 3 = C, 15 = O, 3 = C, 20 = T, 6 = F — confirmed A1Z26 cipher.
### Step 4 - Decode using Boxentriq Numbers to Letters
1. Open Boxentriq at https://www.boxentriq.com/encodings/numbers-to-letters
2. Paste the numbers from inside the curly braces into the input:
   20 8 5 14 21 13 2 5 18 19 13 1 19 15 14
3. Click Decode
Output: THENUMBERSMASON
4. Combine with PICOCTF{} wrapper to get the complete flag
---
## Tools Used
- eog - opening the PNG image to read the number sequence
- Boxentriq Numbers to Letters (https://www.boxentriq.com/encodings/numbers-to-letters)
  converting each number to its corresponding letter position in the alphabet
---
## Flag
PICOCTF{THENUMBERSMASON}
---
## What I Learned
- A1Z26 is a simple substitution cipher where each letter is replaced by its
  position number in the alphabet — A=1, B=2, C=3 all the way to Z=26
- Numbers all falling within the range 1 to 26 is the instant giveaway for
  the A1Z26 cipher
- The curly braces visible in the image were the key hint — they confirmed the
  flag format and made the cipher immediately obvious
- The hint saying the flag is in PICOCTF{} format was important because it
  meant the flag would be in uppercase unlike the usual picoCTF{} lowercase
- Always look at the range of numbers first when a challenge gives a number
  sequence — the range tells you which encoding scheme is being used
