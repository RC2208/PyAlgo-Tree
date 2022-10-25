import hashlib
hash_object = hashlib.sha1(b'Hacktober2022')
hex_dig = hash_object.hexdigest()
print(hex_dig)
