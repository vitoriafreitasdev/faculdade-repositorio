
#pergunta o ano e o ano de nascimento e depois calcula a diferença entre eles
ano = int(input("Ano atual: "))
ano_de_nascimento = int(input("Ano de nascimento: "))
diferenca = ano - ano_de_nascimento

#aqui vamos converter para str para pegar os ultimos dois digitos para saber qual é a decada
#pegamos também os dois primeiros para saber o seculo
digitos = str(ano_de_nascimento)
ultimos_dois = digitos[:-1] + "0"
dois_primeiros = digitos[:2]
seculo = int(dois_primeiros) + 1
decada = int(ultimos_dois)
print(f"Diferença: ",diferenca)
print(f"Decada: ",decada)
print(f"Seculo: ", seculo)

#pegamos uma frase e deixamos tudo minuscula e sem os espaços, substituimos as ultimas duas palavras e depois invertemos 
frase = input("Frase: ").lower().strip()
substituir_palavra = frase[:-2] + "tr"
frase_inversa = substituir_palavra[::-1]
print(f'Frase invertida: ',frase_inversa)