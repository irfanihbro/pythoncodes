import secrets
import string
import math

# Total karakter yang dipakai (kombinasi huruf besar/kecil, angka, dan simbol)
charset = string.ascii_letters + string.digits + string.punctuation  # 26+26+10+32 = 94
entropy_per_char = math.log2(len(charset))  # Mungkin sekitar 6.554 bits per karakter

# Target entropy
target_entropy = 200
needed_length = math.ceil(target_entropy / entropy_per_char)

# Generate password
password = ''.join(secrets.choice(charset) for _ in range(needed_length))

print(f"Password ({needed_length} chars, ~{target_entropy}-bit entropy):\n{password}")