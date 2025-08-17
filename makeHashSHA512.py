import crypt

#first call
print("Create you hash here!!! ")

# step 1 : password
password = input("type the password to generate a hash:")

# step 2 : generate the hash with random salt and SHA-512
hash_test = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

print("Generate hash to test:")
print(hash_test)
