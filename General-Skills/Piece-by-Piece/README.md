# Piece by Piece
**Category:** General Skills
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2025
---
## Description
Can you put the pieces together to find the flag?
**Hints:**
- How do you combine split files in Linux?
- What tool do you use to extract password protected zip files?
---
## Approach
The challenge gave an SSH connection to a remote server. After logging in I
listed the files in the home directory which revealed an instructions.txt file
and several file parts named part_aa, part_ab, part_ac, part_ad and part_ae.
Reading instructions.txt told me that the flag was inside a password protected
ZIP file that had been split into parts and that the password was supersecret.
I inspected part_aa with cat and saw the PK header at the start which is the
magic bytes signature of a ZIP file — confirming the parts were fragments of a
ZIP archive. I used cat with a wildcard to concatenate all parts matching
part_* into a single file called combined.zip in one command. I then used
unzip on combined.zip and entered the password supersecret when prompted which
extracted flag.txt. Reading flag.txt printed the flag.
---
## Solution
### Step 1 - Connect via SSH
```bash
ssh ctf-player@dolphin-cove.picoctf.net -p 61854
```
Enter the password when prompted. Output: Logged into the remote server.
### Step 2 - List the files
```bash
ls
```
Output:
instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
### Step 3 - Read the instructions
```bash
cat instructions.txt
```
Output: Flag is inside a password protected ZIP file split into parts.
Password: supersecret
### Step 4 - Inspect the first part to identify the file type
```bash
cat part_aa
```
Output: PK header visible at the start of the file — confirms these are
fragments of a ZIP archive since PK is the magic bytes signature for ZIP files.
### Step 5 - Combine all parts into a single ZIP file using a wildcard
```bash
cat part_* > combined.zip
```
Breaking this down:
- part_* is a wildcard that matches all files starting with part_ in
  alphabetical order — part_aa, part_ab, part_ac, part_ad, part_ae
- cat reads them all in order and the > operator writes the combined
  output into a new file called combined.zip
- Order is handled automatically by the wildcard expansion
### Step 6 - Extract the ZIP file
```bash
unzip combined.zip
```
Output: Prompted to enter the password
Archive: combined.zip

[combined.zip] flag.txt password:
Type the password and press Enter:
supersecret
Output: flag.txt extracted successfully
### Step 7 - Read the flag
```bash
cat flag.txt
```
Output: Flag printed directly in the terminal!
---
## Tools Used
- ssh - connecting to the remote server to access the challenge files
- cat - reading instructions.txt, inspecting part_aa for the ZIP magic bytes,
  and combining all parts into combined.zip using the part_* wildcard
- unzip - extracting the password protected ZIP archive and entering the
  password supersecret found in instructions.txt when prompted
---
## Flag
picoCTF{z1p_and_spl1t_f1l3s_4r3_fun_8fa833a5}
---
## What I Learned
- Large files are often split into parts for storage or transfer — cat with
  a wildcard can reconstruct them in one command without typing each filename
- The part_* wildcard automatically expands to all matching files in
  alphabetical order which ensures the correct reconstruction sequence
- PK at the start of a file is the magic bytes signature for ZIP archives —
  always check file signatures when dealing with unknown binary files
- unzip without -P prompts interactively for the password which is useful
  when the password is short and easy to type
- Always read instructions.txt or README files first in any challenge — the
  entire solution including the password was spelled out in the instructions
