#imported modules
from Crypto.Cipher import AES
from zlib import crc32

# input and output paths
input_path = "/home/nik/Downloads/venv/ItsOnFire/res/raw/iv.png"
output_path = "/home/nik/Downloads/venv/ItsOnFire/res/raw/flag.png"

# key input strings
s1 = "https://flare-on.com/evillc2server/report_token/report_token.php?token="
s2 = "wednesday"

# AES IV key. Using b makes it into a byte string
iv = b"abcdefghijklmnop"

# slices characters together
sb = s1[4:10] + s2[2:5]          
crc_val = crc32(sb.encode('utf-8'))
key_str = str(crc_val) + str(crc_val)
key = key_str[:16].encode()      

# opens the encrypted file in binary mode, then reads the contents
with open(input_path, "rb") as f:
    data = f.read()

# now throwing it all together using AES and CBC mode with the IV to decrypt the binary data
dec = AES.new(key, AES.MODE_CBC, iv).decrypt(data)

# prints the first 16 bytes
print("Decrypted data starts with:", dec[:16])

# PKCS#7 helps with padding bytes that were added during encryption
# remove PKCS#7 padding
pad_len = dec[-1]
# only allow 1 to 16 bytes if valid
if 1 <= pad_len <= 16:
    dec = dec[:-pad_len]

# Save results to output file path
with open(output_path, "wb") as f:
    f.write(dec)

print("Decryption complete. File saved to:", output_path)

