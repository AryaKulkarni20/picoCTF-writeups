# Binary Digits

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2026

---

## Description
This file doesn't look like much just a bunch of 1s and 0s.
But maybe it's not just random noise. Can you recover anything
meaningful from this?

Hints: None

---

## Approach
When I opened the file I saw a huge wall of 1s and 0s with no
spaces between them. I used CyberChef to decode the binary by
setting the delimiter to None so it reads exactly 8 bits at a
time. The Magic Wand in CyberChef then revealed the output was
actually a JPEG image with the flag written inside.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Inspect the binary content
The file contained a long string of 1s and 0s with no spaces

### Step 3 - Decode using CyberChef
- Went to cyberchef.io
- Pasted the binary into the Input box
- Dragged From Binary into the Recipe
- Set Delimiter to None
- Clicked the Magic Wand on the Output box
- CyberChef rendered it as a JPEG image with the flag inside

### Step 4 - Fix the flag format
The flag appeared with square brackets so changed them
to curly brackets before submitting

---

## Tools Used
- CyberChef - binary decoding and image rendering
- wget - downloading the challenge file in Kali

---

## Flag
picoCTF{h1dd3n_th3_b1n4ry_d4e39e9e}

---

## What I Learned
- Binary data can hide images not just text
- Setting the correct delimiter in CyberChef is important
- The Magic Wand in CyberChef auto detects the output type
- picoCTF flags sometimes show square brackets instead of
  curly brackets and need to be corrected before submitting
