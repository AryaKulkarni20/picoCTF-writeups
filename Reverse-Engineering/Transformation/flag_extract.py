enc = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸形㝦㘲捡㕽"
flag = ""
for char in enc:
	raw = ord(char)
	#Shift right by 8 to get the first character
	first = chr(raw >> 8)
	#Perform a bitwise AND to get the secind character
	second = chr(raw & 0xFF)
	flag += first + second
print(flag)
