x = 10 # Binary: 1010
y = 4 # Binary: 0100
print(x & y) # 0 (1010 & 0100 = 0000)
print(x | y) # 14 (1010 | 0100 = 1110)
print(x ^ y) # 14 (1010 ^ 0100 = 1110)
print(~x) # -11 (This inverts all bits, including the sign bit)
print(x << 1) # 20 (1010 -> 10100) - Multiplied by 2
print(x >> 1) # 5 (1010 -> 0101) - Integer divided by 2
