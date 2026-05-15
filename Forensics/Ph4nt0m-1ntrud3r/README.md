# Ph4nt0m 1ntrud3r

**Category:** Forensics
**Difficulty:** Easy
**Points:** 100
**CTF:** picoCTF 2025

---

## Description
A digital ghost has breached my defenses and my sensitive data
has been stolen! Your mission is to uncover how this phantom
intruder infiltrated my system and retrieve the hidden flag.
Dive into the network traffic, apply the right filters and
show off your forensic prowess to unmask the digital intruder!

**Hints:**
- Time is important

---

## Approach
The challenge gave a PCAP file containing recorded network
traffic. I opened it in Wireshark and followed TCP streams
which revealed Base64 encoded fragments scattered across
multiple packets. I used TShark to extract the TCP segment
data from the packets. I noticed the relevant packets had
specific lengths of either 12 or 4 bytes so I filtered for
those using TShark and piped the output through xxd to
convert the hex data into readable text. This revealed the
Base64 fragments which I decoded using CyberChef and then
reassembled into the final flag.

---

## Solution

### Step 1 - Download the file
wget the challenge file directly into Kali

### Step 2 - Open in Wireshark
wireshark myNetworkTraffic.pcap
Scanned the packet list and followed TCP streams
Found Base64 looking fragments scattered across streams

### Step 3 - Extract TCP segment data using TShark
tshark -r myNetworkTraffic.pcap -T fields -e tcp.segment_data
This extracted all raw TCP segment data from every packet
in hex format showing where the Base64 fragments were hiding

### Step 4 - Filter by packet length and decode hex
tshark -r myNetworkTraffic.pcap -Y "tcp.len==12 || tcp.len==4" -T fields -e tcp.segment_data | xxd -r -p
Breaking this command down:
- -Y "tcp.len==12 || tcp.len==4" filters only packets
  with a length of exactly 12 or 4 bytes which is where
  the relevant data was hiding
- -T fields -e tcp.segment_data extracts just the
  TCP segment data field
- xxd -r -p converts the hex output into readable text
This revealed the Base64 encoded fragments directly
in the terminal

### Step 5 - Identify Base64 fragments
Found these Base64 fragments across the packets:
bnRfdGg0dA==
NjZkMGJmYg==
ezF0X3c0cw==
XzM0c3lfdA==
cGljb0NURg==
YmhfNHJfOQ==
fQ==

### Step 6 - Decode each fragment using CyberChef
- Went to cyberchef.io
- Pasted each Base64 fragment into the Input box
- Applied From Base64 to each one
- Decoded values:
  bnRfdGg0dA==  → nt_th4t
  NjZkMGJmYg==  → 66d0bfb
  ezF0X3c0cw==  → {1t_w4s
  XzM0c3lfdA==  → _34sy_t
  cGljb0NURg==  → picoCTF
  YmhfNHJfOQ==  → bh_4r_9
  fQ==          → }

### Step 7 - Reassemble the flag
Arranged the decoded fragments in the correct order
to form the complete flag

---

## Tools Used
- Wireshark - opening and visually inspecting the PCAP file
- TShark - extracting TCP segment data from packets
- xxd - converting hex output into readable text
- CyberChef - decoding each Base64 fragment

---

## Flag
picoCTF{1t_w4snt_th4t_34sy_tbh_4r_966d0bfb}

---

## What I Learned
- PCAP files store raw network traffic and can hide data
  inside TCP packet payloads
- Wireshark is used for visual inspection of network traffic
- TShark extracts specific fields from packets using filters
- Filtering by packet length tcp.len==12 or tcp.len==4 helps
  narrow down exactly which packets contain relevant data
- xxd -r -p converts raw hex data into readable text
- Flags can be split across multiple packets as Base64
  fragments and need to be reassembled in the correct order
