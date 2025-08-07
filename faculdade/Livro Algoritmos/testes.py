chave = "Olá"
chaveencode = chave.encode()
print(chaveencode)

string = "Olá, mundo!"
bytes_utf8 = string.encode('utf-8')
print(bytes_utf8)
# Saída: b'Ol\xc3\xa1, mundo!'

bytes_latin1 = string.encode('latin-1')
print(bytes_latin1)
# Saída: b'Ol\xe1, mundo!'