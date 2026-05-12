# Corrupted File

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2026

---

## Description
A file has been corrupted. Can you recover it and find the flag?
A couple of bytes could make all the difference.

**Hints:**
- A couple of bytes could make all the difference

---

## Approach
The challenge gave a file with no extension. Running the file
command showed Linux could not identify it at all. I uploaded
the file to CyberChef and used the Magic tool which gave a hint
that the file was a JPEG but the magic bytes were wrong. This
told me I needed to modify the operation arguments before using
hexdump to inspect and fix the corrupted bytes. I used hexdump
to find the exact corruption and then repaired the file by
replacing the wrong bytes with the correct JPEG magic bytes.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Run the file command
file file
Output: file: data
Linux cannot identify the file type at all

### Step 3 - Upload to CyberChef and use the Magic tool
- Went to cyberchef.io
- Uploaded the file into the Input box
- Clicked the Magic Wand tool
- CyberChef hinted that the file was a JPEG but the
  magic bytes were incorrect
- This told me I needed to modify the operation arguments
  before proceeding

### Step 4 - Inspect the hex header using hexdump
hexdump -C file | head
Output: File starts with 5C 78 FF E0
A correct JPEG should start with FF D8 FF E0
The first two bytes 5C 78 are the corruption
They represent the characters backslash x which
should not be there

### Step 5 - Fix the corrupted bytes
(printf '\xff\xd8' && tail -c +3 file) > repaired.jpg
This replaces the wrong first two bytes with FF D8
and saves the fixed file as repaired.jpg

### Step 6 - Confirm the fix
file repaired.jpg
Output: JPEG image data confirmed

### Step 7 - Open the image
xdg-open repaired.jpg
Flag visible inside the image!

---

## Tools Used
- file - checking the file type
- CyberChef Magic tool - identifying the file type hint
- hexdump - inspecting raw bytes of the file
- printf - writing correct magic bytes
- tail - skipping the corrupted bytes
- xdg-open - opening the repaired image

---

## Flag
picoCTF{r3st0r1ng_th3_by73s_2326ca93}

---

## What I Learned
- Every file type has magic bytes at the start that identify it
- JPEG files always start with FF D8 FF E0
- CyberChef Magic tool can hint at the true file type
  even when the magic bytes are wrong
- hexdump lets you inspect the raw bytes of any file
- You can repair corrupted files by replacing wrong magic bytes
- The file command uses magic bytes not the file extension
