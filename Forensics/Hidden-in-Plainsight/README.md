# Hidden in Plainsight

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2026

---

## Description
Something is tucked away out of sight inside the file.
Find the flag hidden within the image.

**Hints:**
- Something is tucked away out of sight

---

## Approach
The challenge gave a JPG image that looked completely normal
when opened. The name Hidden in Plainsight hinted that something
was hidden inside the file itself. I used the file command to
confirm it was a JPEG image. I then used exiftool to read the
metadata and found a Base64 encoded string in the Comment field.
I decoded it using CyberChef which revealed a second Base64
string containing the steghide password. I then ran steghide
info to confirm there was an embedded file inside the image.
Finally I extracted the hidden file using steghide to get the flag.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Check the file type
file img.jpg
Output: Confirmed as a standard JPEG image

### Step 3 - Check metadata with exiftool
exiftool img.jpg
Found a suspicious Base64 string in the Comment field:
c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9

### Step 4 - Decode the first Base64 string using CyberChef
- Went to cyberchef.io
- Pasted the Comment string into the Input box
- Dragged From Base64 into the Recipe
- Output: steghide:cEF6endvcmQ=
- This revealed the tool to use is steghide and there
  is a second Base64 encoded password

### Step 5 - Decode the second Base64 string using CyberChef
- Pasted cEF6endvcmQ= into CyberChef
- Applied From Base64 again
- Output: pAzzword
- This is the steghide password

### Step 6 - Confirm hidden data exists using steghide info
steghide info img.jpg
Entered passphrase: pAzzword
This confirmed that there was an embedded file hidden
inside the image

### Step 7 - Extract hidden data using steghide
steghide extract -sf img.jpg
Entered passphrase: pAzzword
A hidden file was extracted successfully

### Step 8 - Read the flag
cat flag.txt
Flag printed in terminal!

---

## Tools Used
- file - confirming file type
- exiftool - extracting image metadata
- CyberChef - decoding the Base64 strings (two layers)
- steghide info - confirming hidden data exists in the image
- steghide - extracting hidden data from the image

---

## Flag
picoCTF{h1dd3n_1n_1m4g3_54e31417}

---

## What I Learned
- Images can hide data inside them using steganography
- Always check metadata with exiftool in forensics challenges
- Base64 strings can be layered inside each other
- steghide info confirms if a file has hidden data before extracting
- steghide hides files inside images using a password
- The Comment field in image metadata can contain hidden clues
