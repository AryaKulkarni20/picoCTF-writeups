# Open the file (change filename if needed)
with open("digits.bin", "r") as f:
    binary_data = f.read().strip()

# Remove any spaces, newlines just in case
binary_data = binary_data.replace(" ", "").replace("\n", "")

# Read 8 bits at a time and convert to characters
flag = ""
for i in range(0, len(binary_data), 8):
    byte = binary_data[i:i+8]
    flag += chr(int(byte, 2))

print(flag)
