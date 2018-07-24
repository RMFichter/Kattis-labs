import sys

# Get string of binary representation
decimal = int(sys.stdin.readline())
binary = bin(decimal)
# Remove 0b in beginning
binary = binary[2:len(binary)]
# Reverse the string
reversedBinary = binary[::-1]
# Convert back to decimal and print result
reversedDecimal = int(reversedBinary, 2)
print reversedDecimal