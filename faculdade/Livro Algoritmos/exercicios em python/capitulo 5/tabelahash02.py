votaram = {}

valor = votaram.get("tom")

voted = {}

def verifica_eleitor(nome):
    if voted.get(nome):
        print("mande embora")
    else:
        voted[nome] = True
        print("Deixe votar")


verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")

cache = {}

def pefa_pagina(url):
    if cache.get(url):
        return cache[url]
    else:
        dados = pega_dados_do_servidor(url)
        cache[url] = dados
        return dados