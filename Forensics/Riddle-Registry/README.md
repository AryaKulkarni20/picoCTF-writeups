# Riddle Registry

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2026

---

## Description
Hi, intrepid investigator! You have stumbled upon a peculiar PDF
filled with what seems like nothing more than garbled text.
The hint tells us to look beyond the surface and uncover the
flag within the metadata.

**Hints:**
- Visible text is just a decoy
- Look beyond the surface

---

## Approach
When I opened the PDF it showed nothing but garbled nonsense text.
My first instinct was to use cat but that gave unreadable output
since PDFs are binary files. I then used the file command to
confirm it was a PDF. Noticing the hint said to look beyond the
surface I decided to check the metadata using exiftool. The Author
field contained a suspicious Base64 encoded string ending in =
which I decoded to find the flag.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Run cat on the file
cat confidential.pdf
Output: Garbled unreadable text since PDFs are binary files

### Step 3 - Run file command
file confidential.pdf
Output: Confirms it is a PDF document

### Step 4 - Check metadata with exiftool
exiftool confidential.pdf
Found a suspicious Base64 string in the Author field:
cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jMjA3MzY2OX0=

### Step 5 - Decode the Base64 string
echo "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9jMjA3MzY2OX0=" | base64 -d
Flag printed directly in the terminal!

---

## Tools Used
- cat - initial file inspection
- file - confirming file type
- exiftool - extracting PDF metadata
- base64 - decoding the hidden string
- CyberChef - alternative decoding method

---

## Flag
picoCTF{puzzl3d_m3tadata_f0und!_f94300c4}

---

## What I Learned
- PDFs store hidden metadata like Author, Title and Keywords
- Always check file metadata in forensics challenges
- Base64 strings always end with = or == signs
- exiftool is a powerful tool for reading file metadata
- The visible content of a file is not always where the flag is
