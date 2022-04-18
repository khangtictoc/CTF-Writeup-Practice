string = "../" # This string would be double-encoded.
payload = ""
filter = ['.','/']

for c in string:
    if c in filter:
        payload += "%25" + hex(ord(c))[2:]
    else:
        payload += c

print(payload)
