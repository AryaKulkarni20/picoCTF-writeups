# Secret of the Polyglot

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2024

---

## Description
The Network Operations Center picked up a suspicious file.
File type tools give conflicting info. Can you extract all
the information from this strange file?

**Hints:**
- This problem can be solved by just opening the file
  in different ways

---

## Approach
The challenge gave a file called flag2of2-final.pdf. The
filename itself was a clue — flag2of2 meaning this is the
second part of two. Running the file command revealed that
despite the .pdf extension the file was actually a PNG image.
This is called a polyglot file — a file that is valid as
more than one format at the same time. Opening it as a PDF
showed the second half of the flag in the text. Renaming it
to .png and opening it as an image revealed the first half
of the flag visually. Combining both halves gave the complete
flag.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali
File received: flag2of2-final.pdf
Note: The filename flag2of2 hints this is part 2 of 2

### Step 2 - Run the file command
file flag2of2-final.pdf
Output: PNG image data confirmed despite the .pdf extension
This tells us the file is a polyglot - valid as both
PNG and PDF at the same time

### Step 3 - Open the file as a PDF
xdg-open flag2of2-final.pdf
Output: Gibberish text but with a closing curly brace }
at the end - this is the second half of the flag

### Step 4 - Rename the file to PNG and open it
cp flag2of2-final.pdf flag2of2-final.png
xdg-open flag2of2-final.png
Output: An image containing the first half of the flag
is now visible!

### Step 5 - Combine both halves
First half from PNG + Second half from PDF = Complete flag!

---

## Tools Used
- file - revealing the true file type
- xdg-open - opening the file as both PDF and PNG
- cp - copying the file with a new extension

---

## Flag
picoCTF{f1u3n7_1n_pn9_&_pdf_1f991f77}

---

## What I Learned
- A polyglot file is a file that is valid as more than
  one format at the same time
- File extensions can be misleading - always use the
  file command to check the true file type
- The same file can be opened in different ways to reveal
  different hidden information
- File names in CTF challenges often contain hints like
  flag2of2 telling you there are multiple parts
- Magic bytes at the start of a file determine its true
  type not the extension
