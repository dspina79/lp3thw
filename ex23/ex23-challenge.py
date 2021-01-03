# Simple reverse

def reverse_encoding(encoded_bytes, format):
    return encoded_bytes.decode(format, errors = "strict")

# should be "this"
encoded_val = b'\xff\xfe\x00\x00t\x00\x00\x00h\x00\x00\x00i\x00\x00\x00s\x00\x00\x00'
print(reverse_encoding(encoded_val, "utf-32"))