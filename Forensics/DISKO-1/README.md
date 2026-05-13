# DISKO 1

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2026

---

## Description
Can you find the flag in this disk image?
Download the disk image here.

**Hints:**
- Maybe strings could help? If only there was a way to do that?

---

## Approach
The challenge gave a compressed disk image file ending in .gz.
I decompressed it using gzip to get the raw disk image. The
file command confirmed it was a FAT32 filesystem disk image.
Since the hint mentioned strings I used the strings command
to extract all readable text from the disk image and piped
it through grep to filter for the picoCTF flag pattern which
printed the flag directly in the terminal.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Check the file
file disko-1.dd.gz
Output: gzip compressed data confirmed

### Step 3 - Decompress the file
gzip -d disko-1.dd.gz
Output: disko-1.dd extracted successfully

### Step 4 - Check the disk image file type
file disko-1.dd
Output: FAT32 filesystem disk image confirmed

### Step 5 - Extract strings and grep for the flag
strings disko-1.dd | grep picoCTF
Output: Flag printed directly in the terminal!

---

## Tools Used
- file - checking file types
- gzip - decompressing the gz file
- strings - extracting readable text from the disk image
- grep - filtering output to find the flag

---

## Flag
picoCTF{1t5_ju5t_4_5tr1n9_be6031da}

---

## What I Learned
- Disk images can be compressed in gz format and need
  decompressing before analysis
- FAT32 is a filesystem commonly used in flash drives
- The strings command extracts all readable text from
  any file including disk images
- grep is used to filter large amounts of output to
  find exactly what you are looking for
- Piping commands together with | is a powerful way
  to chain tools in Linux
