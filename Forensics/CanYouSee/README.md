# CanYouSee

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2024

---

## Description
How about some hide and seek? Can you find the flag?

**Hints:**
- How to use exiftool?
- Exiftool can be used to view metadata of files

---

## Approach
The challenge gave a zip file containing a JPG image called
ukn_reality.jpg. The image looked completely normal when opened.
I used exiftool to check the metadata and found a suspicious
Base64 encoded string hidden inside the Attribution URL field.
Decoding it using CyberChef revealed the flag. I also found
a one liner command that can extract and decode the flag
directly in the terminal without needing CyberChef.

---

## Solution

### Step 1 - Download and unzip the file
wget the challenge file directly into Kali
unzip unknown.zip
File received: ukn_reality.jpg

### Step 2 - Run the file command
file ukn_reality.jpg
Output: JPEG image data confirmed

### Step 3 - Check metadata with exiftool
exiftool ukn_reality.jpg
Found a suspicious Base64 string in the Attribution URL field:
cGljb0NURntNRTc0RDQ3QV9ISUREM05fNmE5ZjVhYzR9Cg==

### Step 4 - Decode Base64 using CyberChef
- Went to cyberchef.io
- Pasted the Base64 string into the Input box
- Dragged From Base64 into the Recipe
- Flag appeared in the Output box!

### Alternative - One liner command in terminal
exiftool ukn_reality.jpg | grep At | cut -d ":" -f2 | tr -d " " | base64 -d
Breaking this down:
- grep At finds the Attribution URL line
- cut -d ":" -f2 extracts everything after the colon
- tr -d " " removes leading spaces
- base64 -d decodes the Base64 string
Flag printed directly in the terminal!

---

## Tools Used
- file - confirming file type
- exiftool - extracting image metadata
- CyberChef - decoding the Base64 string
- base64 - alternative terminal decoding method
- grep, cut, tr - filtering and cleaning terminal output

---

## Flag
picoCTF{ME74D47A_HIDD3N_3b9209a2}

---

## What I Learned
- Image metadata can contain hidden Base64 encoded strings
- The Attribution URL field in EXIF data can hide flags
- exiftool is essential for forensics challenges involving images
- Piping multiple commands together with | is a powerful
  way to extract and decode data in one step
- Always check all metadata fields not just the obvious ones
