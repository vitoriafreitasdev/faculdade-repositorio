def qualNumMaior(n1, n2):
    if n1 > n2:
        maiorNum = n1
    else:
        maiorNum = n2
    return maiorNum

num1 = int(input("Numero 1:"))
num2 = int(input("numero 2:"))

print("O maior numero é", qualNumMaior(num1, num2))

def qualMenor(*args):
    if not args:  # Verifica se args está vazio
        return None  # Ou poderia lançar um erro, dependendo do caso
    menor = args[0]  # Inicializa com o primeiro elemento
    for num in args:
        if num < menor:

            menor = num
    return menor

print(qualMenor(1, 2, 3, 4, 5, 6,7))