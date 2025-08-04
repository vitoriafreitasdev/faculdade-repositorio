
def numero(n1, n2):
    soma = n1 + n2
    return  soma

numero1 = float(input("Coloque o primeiro valor: "))
numero2 = float(input("Coloque o segundo valor:"))

print(numero(numero1, numero2))

def parOuImpar(num):
    if num % 2 == 0:
        return "Numero é par"
    else:
        return "Numero é impar"


n = int(input("Coloque o numero:"))

print(parOuImpar(n))

def fatorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


number = int(input("Coloque o valor:"))

print(fatorial(number))

s1 = {1, 2, 3, 4, 5, 6}
s2 = {6, 7, 8, 9}

print(s1 & s2)