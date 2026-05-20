# information

**Category:** Forensics
**Difficulty:** Easy
**Points:** 10
**CTF:** picoCTF 2021

---

## Description
Files can always be modified in a secret way. Can you find
the flag? Download the file here.

**Hints:**
- Look at the file in a different way
- Make sure to submit the flag as picoCTF{XXXXX}

---

## Approach
The challenge gave a JPG image of a cat that looked completely
normal when opened. The hint said to look at the file in a
different way so I used exiftool to check the metadata. The
License field contained a suspicious Base64 encoded string.
Decoding it using CyberChef revealed the flag. I also found
a one liner command that extracts and decodes the flag
directly in the terminal without needing CyberChef.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali
File received: cat.jpg

### Step 2 - Run the file command
file cat.jpg
Output: JPEG image data, JFIF standard 1.02
Dimensions: 2560x1598, confirmed valid JPEG

### Step 3 - Check metadata with exiftool
exiftool cat.jpg
Found a suspicious Base64 string in the License field:
cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

### Step 4 - Decode Base64 using CyberChef
- Went to cyberchef.io
- Pasted the Base64 string into the Input box
- Dragged From Base64 into the Recipe
- Flag appeared in the Output box!

### Alternative - One liner command in terminal
exiftool cat.jpg | grep License | cut -d ":" -f2 | tr -d " " | base64 -d
Breaking this down:
- grep License finds the License metadata field
- cut -d ":" -f2 extracts everything after the colon
- tr -d " " removes leading spaces
- base64 -d decodes the Base64 string
Flag printed directly in the terminal!

---

## Tools Used
- file - confirming file type
- exiftool - extracting image metadata
- CyberChef - decoding the Base64 string
- base64, grep, cut, tr - alternative terminal method

---

## Flag
picoCTF{the_m3tadata_1s_modified}

---

## What I Learned
- Image metadata fields like License can hide Base64 strings
- exiftool reveals all metadata fields in an image
- Always check every metadata field not just the obvious ones
- Piping grep, cut, tr and base64 together can extract and
  decode hidden data in a single terminal command
- The file command confirms a files true type regardless
  of what the image looks like when opened
