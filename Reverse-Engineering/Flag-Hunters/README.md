# Flag Hunters
**Category:** Reverse Engineering
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2025
---
## Description
Lyrics jump from verses to the refrain kind of like a subroutine call.
There's a hidden refrain this program doesn't print by default.
Can you get it to print it? There might be something in it for you.
**Hints:**
- The crowd controls what happens next
- What characters does the program treat specially?
---
## Approach
The challenge gave a Python source file called lyric-reader.py and a netcat
connection to a remote server. I downloaded and read the source code first to
understand how the program worked. The script reads a flag from flag.txt and
stores it inside a variable called secret_intro which is placed at the very
beginning of the song before the first REFRAIN. The program plays through the
song verse by verse and pauses at a line called CROWD asking for user input.
Reading the source code carefully I noticed the program splits user input on
semicolons and processes each part as a command in a tiny custom language. The
key command was RETURN which jumps to a specific position in the song. Entering
;RETURN 0 as the crowd input made the program jump back to position 0 which is
the very start of the song where secret_intro and the flag are stored. The flag
printed directly in the terminal on the next loop through.
---
## Solution
### Step 1 - Download the source file
```bash
wget https://challenge-files.picoctf.net/c_verbal_sleep/9f2b86c1e1068d492f783b106f4535aeb137b0c0e31e43351f8cb82a39456a84/lyric-reader.py
```
File received: lyric-reader.py
### Step 2 - Read the source code
```bash
cat lyric-reader.py
```
Key observations from reading the source:
- flag is read from flag.txt and stored in secret_intro variable
- secret_intro is placed at position 0 — the very start of the song
- The song is stored as one big string called song_flag_hunters
- The program splits song into sections on [VERSE] and [REFRAIN] tags
- When it hits a CROWD line it pauses and waits for user input
- User input is split on semicolons and each part is processed as a command
- The RETURN command jumps to a given position in the song
### Step 3 - Connect to the server
```bash
nc verbal-sleep.picoctf.net 54588
```
Output: The program starts printing the song verse by verse and then pauses:
Crowd:
### Step 4 - Enter the payload
When the program pauses at Crowd: type the following and press Enter:
;RETURN 0
Breaking this down:
- The semicolon splits the input into commands
- RETURN 0 tells the program to jump back to position 0 in the song
- Position 0 is secret_intro which contains the flag
Output: The program loops back to the start and prints secret_intro with the
flag visible at the end of the intro block!
---
## Tools Used
- cat - reading the source code to understand the program logic
- nc (netcat) - connecting to the remote server to interact with the program
---
## Flag
picoCTF{70637h3r_f0r3v3r_b248b032}
---
## What I Learned
- Always read the source code fully before connecting to the server — the
  vulnerability was clearly visible in the source
- Semicolons being used as command delimiters in user input is a classic
  unsanitised input vulnerability
- The RETURN command jumping to position 0 exposed the secret_intro that was
  never meant to be printed during normal execution
- Hidden data at position 0 of a string is a common trick in reverse
  engineering challenges — always check what comes before the visible output
- Never trust user input in any program — always sanitise and validate before
  processing it as commands or instructions
