# Verify

**Category:** Forensics
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2024

---

## Description
People keep trying to trick my players with imitation flags.
I want to make sure they get the real thing! I'm going to
provide the SHA-256 hash and a decrypt script to help you
know that my flags are legitimate.

ssh -p 59633 ctf-player@rhea.picoctf.net
Password: 1ad5be0d

**Hints:**
- Checksums let you tell if a file is complete and from the
  original distributor. If the hash doesnt match its a
  different file
- You can create a SHA checksum of a file with sha256sum
  or all files in a directory with sha256sum directory/*
- Remember you can pipe the output of one command to another
  with | Try practicing with the First Grep challenge

---

## Approach
This challenge required SSHing into a remote server. Once
connected I found a directory full of files and a checksum.txt
containing the correct SHA-256 hash. The goal was to find
which file in the directory matched the reference hash and
then run the provided decrypt script on it to get the flag.
I used sha256sum on all files at once and piped the output
through grep to find the matching file instantly.

---

## Solution

### Step 1 - SSH into the challenge server
ssh -p 59633 ctf-player@rhea.picoctf.net
Type yes to confirm the fingerprint
Enter password:1ad5be0d

### Step 2 - List the files
ls
Found three items:
- checksum.txt containing the reference SHA-256 hash
- decrypt.sh script to decrypt the correct file
- files/ directory containing many possible flag files

### Step 3 - Check the reference hash
cat checksum.txt
Output: 5848768e56185707f76c1d74f34f4e03fb0573ecc1ca7b11238007226654bcda

### Step 4 - Find the matching file
sha256sum files/* | grep 5848768e56185707f76c1d74f34f4e03fb0573ecc1ca7b11238007226654bcda
This ran SHA-256 on every file and filtered for the one
that matched the reference hash
The correct filename was printed in the terminal

### Step 5 - Decrypt the matching file
./decrypt.sh files/8eee7195
Flag printed directly in the terminal!

---

## Tools Used
- ssh - connecting to the remote challenge server
- ls - listing available files
- cat - reading the reference hash from checksum.txt
- sha256sum - generating SHA-256 hashes for all files
- grep - filtering output to find the matching hash
- decrypt.sh - decrypting the verified file to get the flag

---

## Flag
picoCTF{trust_but_verify_8eee7195}

---

## What I Learned
- SHA-256 is a hashing algorithm used to verify file integrity
- If two files have the same SHA-256 hash they are identical
- sha256sum can check all files in a directory using wildcard *
- Piping sha256sum output through grep is an efficient way
  to find a specific matching hash among many files
- SSH lets you connect to and work on remote servers
- decrypt.sh scripts are commonly used in CTFs to decode
  encrypted files once you have verified them

## Note
This challenge will provide a seperate hash and password for each instance it creates. Please use the commands according to your instance.
