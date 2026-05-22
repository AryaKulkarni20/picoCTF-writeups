# StegoRSA
**Category:** Cryptography
**Difficulty:** Medium
**CTF:** picoCTF
---
## Description
The public key is gone... but someone might have been careless with the private key.
**Hints:**
- What is steganography?
- Where else can data hide inside an image?
---
## Approach
The challenge gave a JPG image and an encrypted file called flag.enc. The hint about
a missing public key suggested the private key was hidden somewhere. I used the file
command on the image which immediately revealed a suspicious comment field in the JPEG
metadata. I then ran exiftool to extract the full comment which turned out to be a long
hex string. I pasted that hex string into CyberChef and used the From Hex recipe which
decoded it into a complete RSA private key in PEM format. I saved that key to a file
and used openssl to decrypt flag.enc directly.
---
## Solution
### Step 1 - Download the files
wget the challenge files directly into Kali
Files received: image.jpg, flag.enc
### Step 2 - Run the file command
```bash
file image.jpg
```
Output: JPEG image data, comment: "2d2d2d2d2d424547494e..."
A comment field appeared in the output which was suspicious and worth investigating.
### Step 3 - Extract the full comment with exiftool
```bash
exiftool image.jpg
```
Output: Comment field contained a long hex-encoded string
The file command truncated the comment so exiftool was needed to get the full hex string.
### Step 4 - Decode the hex in CyberChef
1. Copy the full hex string from the Comment field
2. Open CyberChef at https://gchq.github.io/CyberChef/
3. Use the From Hex recipe to decode it
Output: A complete RSA private key in PEM format
### Step 5 - Save the private key
```bash
nano pico.pem
```
Paste the decoded key:
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCx0rX0ruL4gO6b
u3r1Zj37nYqEfrfZ3NpNOvzxmUNGzoKdE/fMluB7IPyDS2Af/B8xNbimvajmZDGu
UbD6VqjXOxY0aUpQO6rXPhQeh5+ZKbORQo83r+WdzWVnG39yLr0TgHaY+uSUBO5x
4sgRPpBbs6u2HHEjtk2R+/VjoZE4UgdZu6c1j6wAPFC43lzMTbtJ+MSiM8SaHIJA
3toXPkj3t0HGOVu3KWDKV9Vk4q/ieukM/f1clss5BBV7qG4m7Wuvm1arb9pAheCz
JqkFkihWkDfZyIJkzfOMy3+82zHAOf6iPsrsMo4uDfMp1n6L5E2hlYjpKHlKWfMN
DnYjGSr9AgMBAAECggEADK1lP/m04DsO58bcrACbRCQ14x7GnC9Y198v98hxqatg
1/J7vNf3zodqQTD/PCCFF8TI8og8cZpsiU01JQ/HDzsc6OUlwWUTl69LD2cjW2/D
58P7QmDVqaOiSlDFS/5lh+2lZuAiKiRU3IUqtsIDWCpNwFi0PzPIwXLZSn5TBFUE
RYcq2YX+Ibma8vKdO+WIq+boIsWW3fs3pJyi+/K2UcZ+Q2CXUYn24G53dTZrzKxG
70FmRPB5H2xuA4KwwqvbF4LH3E7+8AkGGk78/F78AhheomgSqUAt7y9zR2vmS/+/
21Ds/tRnt2WktspWpti3uYNWXj7tesKFSZmoxKPMYQKBgQDlOQ8eWiZ5K6Cbs3dk
wlwZMlUZtFRCNVOnwc5Ko1Zv+67C0pXq9SKYrM2bPA2IOPUaSKJmYja2kByzfdOa
4A428hb2bW95JxdECuJbBAhHQGfZCkh2gqRGW09EzLWfNH2qOwHAKYPRI/J+Dynf
kbbhYgHmx7WwlDEqFDN8S/2i3QKBgQDGmIiuId4ri4RXuMlS0/IfYHd9ajzW1lzo
QiYFC2hHMs7B1PoRpXNsogHX4YcsEVk6lNXNEO+onc5AJbVcLmMrvADsnQSZNEg1
jHgDCAv2CjvICU7B9y8hwZDqf1IzsYaPRfNmFYTqjgMRsEChRLN+dDNbeOuu2nVv
ljE9IqXWoQKBgFAGe6C9GHF1Kb0yCpzCviSNzegLbN8wfuQyZTLpk2PFGl4p5u0A
Z/OlYKKxdIf6Wpeyg//6id9ysJJ5e0a2sj+8hQfDbQd+/kBjDGN6JOm7MoYzcNjv
AysM9b+vODk8uiKUNyg/ViXNxvr7kELdPFuzO7a2QlhDZGasZs0eOo6BAoGBAIdE
2Dw7Z1ejpRYXEFHxeUaz70+mcCApTIkKnVjsRy/PxJK0HUyttCv3QWgo/mgevPcw
71vJQGRKcHSy+o/6LKRaXwrLfJlZyiFnN0thTLxehg+ff1yQoDLO5IVFCdmZ/rxR
+hK7b5hP+Hkw4yS1ZckpHt4cQ/QKatkBpTIuCmVhAoGAPuloXDtiveirkWoGqPyS
TJWn5JefEwhxDZ7Ta9qmxjoox0SAOcCUKNIZECY4l9hUtDiwIAcXuJTibTILwHlR
vI8YK+UsUxChFJqDaxfCbYUqt+yvWhOYy4iO8n9rDpa/DNP9/m+j0KoClJYwVkM1
k5Iy7bZWFOtvRW9ZwrxxGhM=
-----END PRIVATE KEY-----
Save and exit with Ctrl+X then Y
### Step 6 - Decrypt the flag
```bash
openssl pkeyutl -decrypt -inkey pico.pem -in flag.enc
```
Output: Flag printed directly in the terminal!
---
## Tools Used
- file - spotting the suspicious comment field in JPEG metadata
- exiftool - extracting the full hex string from the Comment field
- CyberChef - decoding the hex string into the RSA private key
- openssl - decrypting flag.enc using the extracted private key
---
## Flag
picoCTF{rs4_k3y_1n_1mg_3a1b045}
---
## What I Learned
- JPEG files have a Comment metadata field that can store arbitrary hidden data
- The file command can reveal suspicious metadata but exiftool shows the full content
- Hex-encoded data hidden in image comments is a classic steganography technique
- Always run exiftool on image files in CTF challenges as a standard first step
- Private keys embedded in file metadata completely defeat the purpose of encryption
