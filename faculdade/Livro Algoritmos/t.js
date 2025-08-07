
// const musicas = {
//     "Justin Bieber": 141,
//     "Mariah carey": 233,
//     "Black Sabbath": 34,
//     "Queen": 56,
//     "Alice in chains": 76,
//     "Aretha Franklin": 29,
//     "Nirvana": 30
// }
// arr = ["1", "2", "3", "4"]

// for (let musica in musicas){
//     console.log(musicas[musica])
// }


let obj = []

let pessoa1 = {
    nome: "Joao",
    idade: "30",
    profissao: "arquiteto"
}

let pessoa2 = {
    nome: "Ana",
    idade: "21",
    profissao: "RH"
}


obj.push(pessoa1, pessoa2)

for(let i = 0; i <= obj.length - 1; i++){
    console.log(obj[i].nome)
}


console.log(obj)
