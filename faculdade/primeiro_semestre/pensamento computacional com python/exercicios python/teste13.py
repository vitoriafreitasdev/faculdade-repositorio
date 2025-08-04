
print(" CADASTRO INTERATIVO ")
   
# Validação do nome não pode estar vazio
while True:
    nome = input("Digite seu nome: ").strip()
    if nome:
        break
    print("Erro: Nome não pode ser vazio!")
   
# Validação da idade tem ser número positivo
while True:
    idade = int(input("Digite sua idade: "))
    if(idade > 0):
        break
    else:
        print("Idade inválida. Tente novamente.")
           
cidade = input("Digite sua cidade: ").strip()
   
# Exibição
print("DADOS CADASTRADOS")
print(f"Nome: {nome.title()}")
print(f"Idade: {idade} anos")
print(f"Cidade: {cidade.title()}")





