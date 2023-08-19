# kuldeep singh chouhan
#200530

# hw-2/question-1

import random

def message_generator10():
	# generates a 10 bits random message string
    number = random.getrandbits(10)
    binary_string = format(number, '010b')
    return binary_string

def message_generator15():
	# generates a 15 bits random message string
    number = random.getrandbits(15)
    binary_string = format(number, '015b')
    return binary_string

def bitwise_xor(num1,num2):
	ans = ""
	length = len(num2)-1
	while length >= 1:
		if num1[length] == num2 [length]:
			ans = ans + "0"
		else:
			ans = ans + "1"
		length = length - 1
	ans = ans[::-1]
	return ans

def crc_division(intermediate_frame,crc_pattern):
	# crc division
	divisor_length = len(crc_pattern)
	dividend_length = len(intermediate_frame)
	dividend_section = intermediate_frame[0:divisor_length]
	while divisor_length < dividend_length:
		if dividend_section[0] == '1':
			# if 1st bit is 1, subtract(modulo 2) the divisor and add the next bit to the answer
			dividend_section = bitwise_xor(crc_pattern,dividend_section) + intermediate_frame[divisor_length]
		else:
			# if 1st bit is 0, bring add the next bit to the dividend section
			dividend_section = bitwise_xor('0'*divisor_length,dividend_section) + intermediate_frame[divisor_length]
		divisor_length = divisor_length + 1

	if dividend_section[0] == "1":
		dividend_section = bitwise_xor(crc_pattern,dividend_section)
	else:
		dividend_section = bitwise_xor('0'*divisor_length,dividend_section)

	remainder = dividend_section 
	return remainder

def get_frame(data_block,crc_pattern):

	# adding n-k+1 0s at the end
	divisor_length = len(crc_pattern)
	intermediate_frame = data_block + '0'*(divisor_length-1)

	# attach the remainder to the end of data block
	remainder = crc_division(intermediate_frame,crc_pattern)
	final_frame = data_block + remainder
	return final_frame


print("\n------------------\n")

data_block = input("Enter Data block: ")
crc_pattern = input("Enter CRC pattern: ")

print("The encoded frame is: ", get_frame(data_block,crc_pattern))

print("\n------------------\n")

data1 = message_generator10()
crc1 = "110101"
T = get_frame(data1,crc1)
print("Message generated: ",data1)
print("CRC pattern: ",crc1)
print("The encoded frame is: ",T)

print("\n------------------\n")


# creating error according to a random error pattern
error_bit = 0
T1 = ""
error_pattern = message_generator15()
for c in error_pattern:
	if c=='1':
		T1 = T1 + str(1^int(ord(T[error_bit])-ord('0')))
	else:
		T1 = T1 + T[error_bit]
	error_bit = error_bit+1

print("Error pattern:   ", error_pattern)
print("Erroneous frame: ",T1)
print("Correct frame:   ",T)

print("\n------------------\n")

# error detection
print("remainder: ", crc_division(T1,crc1))
if crc_division(T1,crc1) == "00000":
	print("No error detected, frame accepted")
else:
	print("Error detected, frame rejected")

print("\n------------------\n")



# sample test output 1
# ------------------

# Enter Data block: 11100011
# Enter CRC pattern: 10011    
# The encoded frame is:  111000110110

# ------------------

# Message generated:  1100101111
# CRC pattern:  110101
# The encoded frame is:  110010111100111

# ------------------

# Error pattern:    101111001001001
# Erroneous frame:  011101110101110
# Correct frame:    110010111100111

# ------------------

# remainder:  00000
# No error detected, frame accepted

# ------------------


# sample test output 2
# ------------------

# Enter Data block: 10010011011
# Enter CRC pattern: 10011
# The encoded frame is:  100100110111100

# ------------------

# Message generated:  0011101010
# CRC pattern:  110101
# The encoded frame is:  001110101011100

# ------------------

# Error pattern:    010000000101011
# Erroneous frame:  011110101110111
# Correct frame:    001110101011100

# ------------------

# remainder:  10011
# Error detected, frame rejected

# ------------------

