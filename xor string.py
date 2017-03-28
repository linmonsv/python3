import binascii

buf1 = b"\x12\x34\x56\x78\x11\x22\x33\x44"
buf2 = b"\x11\x22\x33\x44\x55\x66\x77\x88"

print(binascii.b2a_hex(buf1))
print(binascii.b2a_hex(buf2))

res = []
for i in range(0, 8):
    res.append("%02X" % (buf1[i] ^ buf2[i]))
print("".join(res))
