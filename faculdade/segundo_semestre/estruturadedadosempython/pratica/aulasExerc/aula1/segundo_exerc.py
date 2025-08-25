nome = input("Seu nome: ").strip()

qtd = int(input("Quantas valores você vai digitar: "))

soma = 0.0 

for i in range(qtd):
    valor = float(input("Valor: "))
    soma = soma + valor 

media = soma / qtd

if media >= 70:
    status = "Excelente"
elif 50 <= media <= 69:
    status = "Bom"
else: 
    status = "Precisa melhorar"

print("\n ---- resultado ---- ")
print(f"Aluno(a): {nome}")
print(f"Media: {media:.2f}")
print(f"Classificação: {status}")