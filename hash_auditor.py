import hashlib

# Target hash to audit
#target_hash= "8d679db91efa64f5e0ad33c7d16b0c469aa675a7263273b24e2184f986d17d1c"
salt = "mysalt99"
real_password = "raihan143"

#How save the hash with salt
target_hash =hashlib.sha256((salt + real_password).encode("utf-8")).hexdigest()

# For audit a weak password dictionary list
common_passwords = ["12345", "passwaord123", "raihan143", "raihan"]

print(f"Target Salted Hash: {target_hash}")

for password in common_passwords:
    generated_hash = hashlib.sha256((salt + password).encode("utf-8")).hexdigest()
    if generated_hash == target_hash:
        print(f"Password found: {password}")
        break
else:
    print("Password not found in dictionary.")    