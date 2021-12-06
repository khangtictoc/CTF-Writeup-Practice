string = "00000020.0804b160.0804853d.00000009.bffffcc5.b7e1b589.bffffb94.b7fc3000.b7fc3000.0804b160.39617044.28293664.6d617045.bf000a64.0804861b.00000002.bffffb94.bffffba0.cfa6f800.bffffb00.00000000.00000000.b7e03f21.b7fc3000.b7fc3000.00000000.b7e03f21.00000002.bffffb94.bffffba0.bffffb24.00000001."
newstring = string.replace(".","")
print(newstring)
ba = bytearray.fromhex(newstring)
print(ba)
ba.reverse()

s = ''.join(format(x, '02x') for x in ba)
print(s.upper())
