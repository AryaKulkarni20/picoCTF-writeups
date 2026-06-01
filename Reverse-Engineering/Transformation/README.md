# Transformation
**Category:** Reverse Engineering
**Difficulty:** Easy
**Points:** 20
**CTF:** picoCTF 2021
---
## Description
I wonder what this really is...
enc
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
**Hints:**
- You may find some decoders online
- UTF-8 has some interesting properties
---
## Approach
The challenge gave an encoded file called enc and a Python one-liner in the
description that showed how the flag was encoded. I used the cat command to read
the enc file but the contents displayed as strange Chinese-looking characters
which confirmed the file contained multi-byte Unicode characters. Reading the
encoding one-liner carefully I understood that it takes two characters of the
flag at a time, shifts the first character left by 8 bits and adds the second
character to pack both ASCII values into a single Unicode character. To reverse
this I wrote a Python script called flag_extract.py that hardcoded the encoded
string directly, looped through each Unicode character, right shifted by 8 bits
to get the first original character and applied a bitwise AND with 0xFF to
extract the lower 8 bits for the second original character. Running the script
decoded the string and printed the flag directly in the terminal.
---
## Solution
### Step 1 - Download the file
```bash
wget https://artifacts.picoctf.net/c/387/enc
```
File received: enc
### Step 2 - Read the enc file
```bash
cat enc
```
Output: 灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽
Strange Chinese-looking Unicode characters confirmed the file contains packed
multi-byte Unicode and not plain ASCII text.
### Step 3 - Understand the encoding one-liner
The encoding formula from the challenge description:
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
Breaking this down:
- ord(flag[i]) gets the ASCII value of the first character
- << 8 shifts it left by 8 bits which is the same as multiplying by 256
- ord(flag[i + 1]) adds the ASCII value of the second character
- Both values are packed into one Unicode character using chr()
- Two ASCII characters become one Unicode character
### Step 4 - Write the Python decode script
```bash
nano flag_extract.py
```
Paste the following content:
enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"
flag = ""
for char in enc:
	raw = ord(char)
	#Shift right by 8 to get the first character
	first = chr(raw >> 8)
	#Perform a bitwise AND to get the second character
	second = chr(raw & 0xFF)
	flag += first + second
print(flag)
Save and exit with Ctrl+X then Y
### Step 5 - Run the script
```bash
python3 flag_extract.py
```
Output: Flag printed directly in the terminal!
---
## Tools Used
- cat - reading the enc file to observe the Unicode characters
- Python3 - writing flag_extract.py to unpack each Unicode character back into
  two ASCII characters using right bit shifting and bitwise AND masking
---
## Flag
picoCTF{16_bits_inst34d_of_8_b7f62ca5}
---
## What I Learned
- Always read the encoding formula in the challenge description carefully —
  it tells you exactly how to reverse the transformation
- Left shifting by 8 bits packs two ASCII characters into one Unicode character
  and right shifting by 8 bits unpacks them back
- cat showing strange Unicode characters on an encoded file is the immediate
  signal that multi-byte encoding or bit packing is involved
- The bitwise AND with 0xFF is the standard way to extract the lower 8 bits
  from any integer value
- Reversing a custom encoding is simply a matter of undoing each operation in
  the opposite order — shift left becomes shift right, add becomes mask
