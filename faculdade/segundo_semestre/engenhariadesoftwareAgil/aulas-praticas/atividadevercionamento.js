
linhas = 10

// externo é a label
externo: for (let l = 1; l <= linhas; l++){
    let linha = ""
    interno: for (k = 1; k <= l; k++){
        linha += "*"
    }
    if(l > linha){
        break externo // faz uma referência a label
    }
    console.log(linha)
}


