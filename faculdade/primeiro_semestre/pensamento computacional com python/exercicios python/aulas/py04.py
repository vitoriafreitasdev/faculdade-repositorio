print ("Olá competidor, Digite a sua idade > 5")
nome = input ("Qual o seu nome?")
idade = int (input("Qual a sua idade:"))
if idade >=5 and idade <=7 :
    print(f"{nome} Infanti A")
elif idade >=8 and idade <= 10 :
    print (f"{nome} Infantil B")
elif idade >=11 and idade <=13 :
    print (f"{nome} juvenil A")
elif idade >=14 and idade <=17 :
    print (f"{nome} Juvenil B")
elif idade >=17 :
      print (f"{nome} Senior")
else:
     print (f"{nome} Não encotrado")
