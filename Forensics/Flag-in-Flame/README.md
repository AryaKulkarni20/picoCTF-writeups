# Flag in Flame

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2026

---

## Description
The SOC team discovered a suspiciously large log file after a
recent breach. When they opened it, they found an enormous block
of encoded text instead of typical logs. Could there be something
hidden within? Your mission is to inspect the resulting file and
reveal the real purpose of it.

**Hints:** Use base64 to decode the data and generate the image file

---

## Approach
The challenge gave a large logs.txt file full of what looked
like random characters. The description hinted at encoded text
so I used the file command to confirm it was a text file. The
contents looked like Base64 so I decoded it which revealed a
JPEG image. Opening the image showed a hex string at the bottom
which I decoded to get the final flag.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Inspect the file
cat logs.txt
Output: Massive wall of encoded characters

### Step 3 - Check the file type
file logs.txt
Output: Confirmed as a text file with encoded data

### Step 4 - Decode Base64 to image
base64 -d logs.txt > decoded_FlagInFlames.jpg
Converted the Base64 text into a JPEG image file

### Step 5 - Confirm it is an image
file decoded_FlagInFlames.jpg
Output: JPEG image data confirmed

### Step 6 - Open the image
xdg-open decoded_FlagInFlames.jpg
Image showed a cyber man with a long hex string at the bottom

### Step 7 - Decode the hex string
echo "7069636F43544678666F72656E736963735F616E616C797369735F69735F6160617A696E675F373832653535633970" | xxd -r -p
Output: Flag printed in terminal!

---

## Alternative Method - Using CyberChef

You can also solve this entirely in CyberChef:

1. Go to cyberchef.io
2. Paste the contents of logs.txt into the Input box
3. Drag From Base64 into the Recipe
4. Click the Magic Wand on the Output box - it will
   automatically render the output as a JPEG image
5. The hex string will be visible at the bottom of the image
6. Add From Hex into the Recipe after From Base64
7. The flag will appear in the Output box

---

## Tools Used
- cat - inspecting raw file contents
- file - confirming file types
- base64 - decoding the Base64 encoded log file
- xdg-open - opening the decoded image
- xxd - decoding the hex string to get the flag
- CyberChef - alternative method for full decoding

---

## Flag
picoCTF{forensics_analysis_is_amazing_782e55c9}

---

## What I Learned
- Large log files can hide Base64 encoded images inside them
- Always check what type of data is encoded in a file
- Flags can be hidden in two layers - Base64 then Hex
- xxd -r -p is used to convert hex strings to readable text
- The Magic Wand in CyberChef auto detects output types
- Real world attackers disguise data as normal looking logs
