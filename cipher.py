# Importing libraries
from Crypto.Cipher import AES
from zlib import crc32

# Input and output paths
input_path = "/home/nik/Downloads/venv/ItsOnFire/res/raw/iv.png"
output_path = "/home/nik/Downloads/venv/ItsOnFire/res/raw/flag.png"

# Key input strings
s1 = "https://flare-on.com/evilc2server/report_token/report_token.php?token="
s2 = "wednesday"

# AES IV — must be exactly 16 bytes
iv = b"abcdefghijklmnop"

# Generate AES key from crc32 of combined string
key_part = s1[4:10] + s2[2:5]
crc = f"{crc32(key_part.encode()):08x}" * 2
key = crc[:16].encode()

# Decrypt the encrypted file
with open(input_path, "rb") as f:
    data = f.read()

dec = AES.new(key, AES.MODE_CBC, iv).decrypt(data)

# Print first few bytes to help debug
print("Decrypted data starts with:", dec[:16])

# Validate and strip PKCS#7 padding
pad_len = dec[-1]
if 1 <= pad_len <= 16:
    dec = dec[:-pad_len]

# Save the decrypted result
with open(output_path, "wb") as f:
    f.write(dec)

print("Decryption complete. File saved to:", output_path)

