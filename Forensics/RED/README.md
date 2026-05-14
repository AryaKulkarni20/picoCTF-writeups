# RED

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2025

---

## Description
You have a red image. Can you find the flag hidden within it?

**Hints:** None

---

## Approach
The challenge gave a PNG image that appeared to be completely
plain red when opened. I used exiftool to check the metadata
and found a poem hidden in it. Taking the first letter of each
line of the poem and reading them together spells CHECK LSB
which told me exactly where to look. LSB stands for Least
Significant Bit which is a steganography technique that hides
data in the last bit of each pixel. I used zsteg to extract
the hidden data from the image which revealed a Base64 encoded
string. Decoding it in CyberChef gave me the flag.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Check the file type
file RED.png
Output: PNG image data confirmed

### Step 3 - Check metadata with exiftool
exiftool RED.png
Found a poem hidden in the metadata:

Crimson heart, vibrant and bold,
Hearts flutter at your sight.
Evenings glow softly red,
Cherries burst with sweet life.
Kisses linger with your warmth.
Love deep as merlot.
Scarlet leaves falling softly,
Bold in every stroke.

Taking the first letter of each line spells:
C - Crimson
H - Hearts
E - Evenings
C - Cherries
K - Kisses
L - Love
S - Scarlet
B - Bold

= CHECK LSB

This is the hint telling us to look at the
Least Significant Bits of the image!

### Step 4 - Run zsteg to extract hidden LSB data
zsteg RED.png
Output: A suspicious Base64 string found:
==cGJjb0NURntyM2RfMXNfdGgzX3VsdDFtNHQzX2N1cjNfZjByXzU0ZG4zNTVfFQ==

### Step 5 - Decode Base64 using CyberChef
- Went to cyberchef.io
- Pasted the Base64 string into the Input box
- Dragged From Base64 into the Recipe
- Flag appeared in the Output box!

---

## Tools Used
- file - confirming file type
- exiftool - finding the hidden poem in the metadata
- zsteg - extracting hidden LSB data from the PNG
- CyberChef - decoding the Base64 string

---

## Flag
picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

---

## What I Learned
- Metadata can contain hidden hints not just technical info
- Always read metadata carefully as clues can be hidden
  in plain sight inside poems or comments
- LSB steganography hides data in the least significant
  bits of each pixel which is invisible to the human eye
- zsteg is the best tool for detecting hidden data in
  PNG and BMP files
- The first letters of each line of a poem can spell
  out a hidden message called an acrostic poem
