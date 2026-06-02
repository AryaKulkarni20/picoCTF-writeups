# vault-door-training
**Category:** Reverse Engineering
**Difficulty:** Easy
**Points:** 50
**CTF:** picoCTF 2019
---
## Description
Your mission is to enter Dr. Evil's vault and retrieve the top-secret evil plans.
Each vault door is controlled by a computer and requires a password to open.
Unfortunately, our undercover agents have not been able to obtain the secret
passwords for the vault doors, but one of our junior agents obtained the source
code for each vault's computer! You will need to read the source code for each
level to figure out what the password is for that vault door. As a warmup, we
have created a replica vault in our training facility. The source code for the
training vault is here: VaultDoorTraining.java
**Hints:**
- The password is revealed in the program's source code
- This problem can be solved without any coding
---
## Approach
The challenge gave a single Java source file called VaultDoorTraining.java. The
hint said the password is revealed in the source code and no coding is needed.
I used the cat command to read the Java file and traced the execution flow. The
main method takes user input, strips the picoCTF{ prefix and the trailing }
using substring before passing the remaining string to the checkPassword method.
Reading the checkPassword method I found it simply compares the input directly
against a hardcoded string. The password was sitting in plain sight inside the
return statement — no decompiling, no debugging and no scripting required. I
wrapped it in the picoCTF{} format and that was the flag.
---
## Solution
### Step 1 - Download the file
```bash
wget https://artifacts.picoctf.net/c/14/VaultDoorTraining.java
```
File received: VaultDoorTraining.java
### Step 2 - Read the source code
```bash
cat VaultDoorTraining.java
```
Output: Full Java source code printed to the terminal
### Step 3 - Analyse the main method
The main method does the following:
- Prompts the user to enter a vault password
- Strips the picoCTF{ prefix and trailing } from the input using substring
- Passes the remaining string to the checkPassword method
```java
String input = userInput.substring("picoCTF{".length(), userInput.length()-1);
if (vaultDoor.checkPassword(input)) {
    System.out.println("Access granted.");
}
```
### Step 4 - Find the password in checkPassword method
Scrolling down to the checkPassword method reveals the password hardcoded in
plain text inside the return statement:
```java
public boolean checkPassword(String password) {
    return password.equals("w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt");
}
```
The password is sitting in plain sight — no coding needed.
### Step 5 - Wrap the password in the flag format
Combine the hardcoded password with the picoCTF{} wrapper:
picoCTF{w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt}
---
## Tools Used
- cat - reading the Java source file to find the hardcoded password in the
  checkPassword method
---
## Flag
picoCTF{w4rm1ng_Up_w1tH_jAv4_000wYdiGTvt}
---
## What I Learned
- Always read the source code fully before attempting anything complex —
  the password was hardcoded in plain text and visible immediately
- The substring call in the main method strips picoCTF{ and } before checking
  so the checkPassword method only ever sees the inner part of the flag
- Hardcoded credentials in source code is one of the most common and critical
  security vulnerabilities in real world applications
- Reverse engineering does not always mean complex disassembly or debugging —
  sometimes reading the source code is all it takes
- The hint saying this can be solved without any coding was the key signal to
  just read the source carefully rather than writing a script
