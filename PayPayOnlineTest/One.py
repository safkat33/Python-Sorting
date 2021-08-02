import sys

# Use default values
# for line in sys.stdin:
#     line = line.rstrip()
line = "11111010,10010110"
binary_string_list = line.split(",")
a = binary_string_list[0]
b = binary_string_list[1]

# Calculate the max_length between the both strings
max_len = max(len(a), len(b))

# Fill the string with zeros until it is equal to max_len
a = a.zfill(max_len)
b = b.zfill(max_len)

# Initialize the result
result = ''

# Initialize the carry
carry = 0

# Traverse the string
for i in range(max_len - 1, -1, -1):
    r = carry
    r += 1 if a[i] == '1' else 0
    r += 1 if b[i] == '1' else 0
    result = ('1' if r % 2 == 1 else '0') + result

    # Calculate carry.
    carry = 0 if r < 2 else 1

if carry != 0:
    result = '1' + result
binary_sum = result.zfill(max_len)

# Strip leading '0'
binary_sum_striped = binary_sum.strip(" 0")

print(binary_sum_striped)

print((bin(int(a, 2) + int(b, 2))[2:]).strip("0"))
