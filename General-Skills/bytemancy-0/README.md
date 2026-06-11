# bytemancy 0
**Category:** General Skills
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2025
---
## Description
Can you practice your byte manipulation skills?
**Hints:**
- What is ASCII encoding?
- How do you convert a decimal value to a character?
---
## Approach
The challenge connected to a remote server via netcat which printed a prompt
asking to send ASCII DECIMAL 101, 101, 101 side by side with no spaces. ASCII
decimal 101 is the character e — decimal 101 maps to hex 0x65 which is the
lowercase letter e. This is a simpler version of bytemancy-1 since it only
requires sending e three times. I connected to the server and simply typed eee
directly into the terminal. The server compared the input against the string
\x65\x65\x65 which is exactly eee and since they matched it printed the flag
immediately.
---
## Solution
### Step 1 - Connect to the server
```bash
nc candy-mountain.picoctf.net 57689
```
Output: Server printed the challenge prompt
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==>
### Step 2 - Identify what ASCII decimal 101 is
ASCII decimal 101 = hex 0x65 = the character e
The server checks input against \x65\x65\x65 which is exactly eee.
Only 3 characters needed — no automation required, type it directly.
### Step 3 - Enter the answer
Type the following and press Enter:
eee
Output: Flag printed directly in the terminal!
---
## Tools Used
- nc (netcat) - connecting to the remote server and sending the answer
  directly by typing eee into the terminal
---
## Flag
picoCTF{pr1n74813_ch4r5_184029cd}
---
## What I Learned
- ASCII decimal 101 maps to hex 0x65 which is the lowercase letter e —
  knowing the ASCII table is essential for byte manipulation challenges
- The server was checking input against the hex string \x65\x65\x65 which
  is the same as typing eee since each \x65 is just the character e
- bytemancy-0 only needs 3 characters so it can be solved by typing
  directly — unlike bytemancy-1 which needs 1751 characters and requires
  automation with a Python one liner
- Decimal, hex, and ASCII character representations are three ways to
  express the same value — 101 decimal = 0x65 hex = e character
- Always check the ASCII table first when a challenge asks for a decimal
  value — the answer is usually a simple printable character
