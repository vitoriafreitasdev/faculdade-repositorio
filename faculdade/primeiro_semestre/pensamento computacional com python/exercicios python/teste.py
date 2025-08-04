
a = 2
b = 4
print(a + b)
c = 4.5
d = 5.9
print(c + d)
e = 5 + 6j
f = 3 - 4j
print(e + f)
nome = "Gabriella"
print(f"Olá, {nome}")

lista = [4, 8, 6, 10, 2] 
num = 0 
soma = 0 
while num <= 4:
    soma = soma + lista[num] #adição do elemento da lista
    num += 1 # Incremento correto de num
print("Soma:", soma)

num1 = int(input('valor: '))
num2 = int(input('valor: '))
soma = num1 + num2
print(f'soma: {soma}')

x = int(input("Digite um número: ")) # Solicita um número ao usuário
if x > 0:
 print("x é positivo")
elif x < 0:
 print("x é negativo")
else:
 print("x é zero")

numeros = [1, 2, 3]
for numero in numeros:
    print(f"Número: {numero}")
    if numero == 1 or numero == 2:
        continue
    if numero == 3:
        break

print("Acabou")