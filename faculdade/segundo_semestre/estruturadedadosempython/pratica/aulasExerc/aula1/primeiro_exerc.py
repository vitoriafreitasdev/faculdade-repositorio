vezes = int(input("Quantas vezes você vai digitar: "))

for i in range(1, vezes + 1):
    num = int(input("Digite um numero: "))
    if(num % 2 == 0):
        print(f"{num} é par.")
    else: 
        print(f"{num} é impar")