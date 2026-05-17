# Scan Surprise

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2024

---

## Description
I have gotten bored of handing out flags as text. Wouldn't it
be cool if they were an image instead?

ssh -p 54043 ctf-player@atlas.picoctf.net
Password: 1db87a14

**Hints:**
- QR codes are a way of encoding data. While they are most
  known for storing URLs they can store other things too
- Mobile phones have included native QR code scanners in
  their cameras since Android 8 Oreo and iOS 11
- If you dont have access to a phone you can also use
  zbar-tools to convert an image to text

---

## Approach
The challenge gave access to a remote server via SSH. Once
connected I found a file called flag.png which turned out to
be a QR code image. Instead of scanning it with a phone I
used zbar-tools on the command line which is a tool that can
decode QR codes directly in the terminal. Running zbarimg on
the file printed the flag instantly.

---

## Solution

### Step 1 - SSH into the challenge server
ssh -p 54043 ctf-player@atlas.picoctf.net
Type yes to confirm the fingerprint
Enter password: 1db87a14

### Step 2 - List the files
ls
Found: flag.png - a QR code image

### Step 3 - Install zbar-tools
sudo apt install zbar-tools -y
This installs zbarimg which can decode QR codes
directly from the command line

### Step 4 - Decode the QR code
zbarimg --raw flag.png
Output: Flag printed directly in the terminal!

---

## Tools Used
- ssh - connecting to the remote challenge server
- ls - listing available files
- zbar-tools - decoding the QR code from the command line

---

## Flag
picoCTF{p33k_@_b00_b5ce2572}

---

## What I Learned
- QR codes can store any type of data not just URLs
- zbarimg from zbar-tools can decode QR codes in the terminal
  without needing a phone or online tool
- SSH gives you access to remote challenge servers in picoCTF
- Always check what files are available with ls after SSHing in
- Flags can be hidden inside QR code images
