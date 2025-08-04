anos = [1822, 1888, 1932]

intervencoes = {
    1822: ['jafaisfjaipfj', 'faikfosiafsao'],
    1888: ['opujpojpo', 'lpjpojo'],
    1932: ['gdsagdsg', 'sgdsgsd']
}

cont = 1

for ano in anos:

    for intervencao in intervencoes[ano]:
        print(f"linha temporal {cont}: no ano {ano}, ação realizada: {intervencao}.")
        cont += 1
