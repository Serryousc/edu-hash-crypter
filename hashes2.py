import crypt


#hash armazenado
print("type your hash below in the format salt+hash")
stored_hash = input("type your hash here:")

#wordlist de exemplo
wordlist = ["123456", "senha", "admin", "ExemploForte!2025", "Segredo123"]

#inicio laço for

for candidate in wordlist:
	# Replica a estrutura salt+identificador
	test_hash = crypt.crypt(candidate, stored_hash)
	
	if test_hash == stored_hash:
		print(f"senha encontrada: {candidate}")
		break
else:
	print("Nenhuma senha da wordlist bateu.")
	
