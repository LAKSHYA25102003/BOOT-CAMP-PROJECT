import hashlib
print('give input:')
x = input("")
#hashing by SHA256 algorithm from hashlib
hash_object = hashlib.sha256(x.encode())
hex_dig = hash_object.hexdigest()
print("SHA-256 hash:", hex_dig)
#hashing by MD5 algorithm from hashlib
result = hashlib.md5(x.encode()).hexdigest()
print("MD5 hash:",result)
#hashing by SHA512 algorithm from hashlib
output=hashlib.sha512(x.encode()).hexdigest()
print("SHA-512 hash:",output )
