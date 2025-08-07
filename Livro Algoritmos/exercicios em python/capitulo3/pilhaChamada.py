def sauda(nome):
    print( "Ola, " + nome + "!")
    sauda2(nome)
    print("preparando para dizer tchau...")
    tchau()

def sauda2(nome):
    print("Como vai " + nome + "?")
def tchau():
    print("ok, tchau")


sauda("Vitoria")