# Glory of the Garden

**Category:** Forensics
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2019

---

## Description
This garden contains more than it seems.

**Hints:**
- What is a hex editor?

---

## Approach
The challenge gave a JPG image of a garden that looked
completely normal when opened. The hint mentioned a hex
editor which suggested hidden data inside the file. I
used the file command to confirm it was a JPEG. I then
ran the strings command which extracts all readable text
embedded inside a binary file and piped it through grep
to filter for the picoCTF flag pattern. The flag was
hidden as plain text at the end of the image file and
printed directly in the terminal.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali
File received: garden.jpg

### Step 2 - Run the file command
file garden.jpg
Output: JPEG image data confirmed

### Step 3 - Run strings and grep for the flag
strings garden.jpg | grep picoCTF
Breaking this down:
- strings extracts all readable text from the binary file
- grep pico filters the output to only show lines
  containing the word pico
Output: Flag printed directly in the terminal!

---

## Tools Used
- file - confirming file type
- strings - extracting readable text from the binary file
- grep - filtering output to find the flag

---

## Flag
picoCTF{more_than_m33ts_the_3y339cbe6dc}

---

## What I Learned
- Binary files like JPEGs can have plain text hidden
  inside them at the end of the file
- The strings command extracts all readable text from
  any binary file
- Piping strings output through grep instantly finds
  the flag without reading through thousands of lines
- Always run strings and grep on image files in
  forensics challenges as a standard first step
