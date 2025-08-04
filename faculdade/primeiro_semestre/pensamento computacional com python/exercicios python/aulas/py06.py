saldo = 1000
while True:
    try:
        saque = float(input("Digite o valor p/ saque (ou 0 p/ sair)"))
        if saque <= 0: 
           print ("Operação Finalizada.")
           break
        elif saque > saldo:
           print ("Saldo Insuficiente.")
        else:
          saldo -= saque
          print (f"Saque realizado: R${saldo:.2f}")
    except ValueError:
       print("Por favor, insira um número válido")      
