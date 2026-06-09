# bytemancy 1
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
- Can you automate sending a large number of characters?
---
## Approach
The challenge connected to a remote server via netcat which printed a prompt
asking to send ASCII DECIMAL 101 exactly 1751 times side by side with no
spaces. ASCII decimal 101 is the character e — this is straightforward to
verify since the ASCII table maps decimal 101 to the lowercase letter e.
The challenge was that manually typing e 1751 times is impossible so I used
a Python one liner to generate the string and piped it directly into the
netcat command. The python3 -c command generates the string of 1751 e
characters and the pipe sends it straight to the server as input. The server
received the correct input and printed the flag immediately.
---
## Solution
### Step 1 - Connect to the server and read the prompt
```bash
nc foggy-cliff.picoctf.net 63716
```
Output: Server printed the challenge prompt
⊹──────[ BYTEMANCY-1 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==>
### Step 2 - Identify what ASCII decimal 101 is
ASCII decimal 101 = hex 0x65 = the character e
Typing e 1751 times manually is not feasible — automate it with Python.
### Step 3 - Send the payload using a Python one liner piped into netcat
```bash
python3 -c 'print("e"*1751)' | nc foggy-cliff.picoctf.net 63716
```
Breaking this down:
- python3 -c runs a Python command directly from the terminal
- print("e"*1751) generates a string of exactly 1751 e characters
- The pipe | sends the output directly to netcat as input
- netcat forwards it to the server as the answer
Output: Flag printed directly in the terminal!
---
## Tools Used
- nc (netcat) - connecting to the remote server to read the challenge prompt
- python3 -c - generating the payload of 1751 e characters in one line
- pipe (|) - sending the Python output directly into netcat as server input
---
## Flag
picoCTF{h0w_m4ny_e's???_6e0cc4c6}
---
## What I Learned
- ASCII decimal 101 maps to the character e — knowing the ASCII table is
  essential for any byte manipulation challenge
- python3 -c with string multiplication is the fastest way to generate
  large repetitive payloads without writing a full script
- Piping python3 output directly into netcat is a powerful technique that
  eliminates the need to type long inputs manually into a server
- The challenge title bytemancy hints at byte manipulation — always check
  the ASCII table first when a challenge asks for decimal values
- Automating repetitive input with one liners is a core general skills
  technique used constantly in CTF challenges
