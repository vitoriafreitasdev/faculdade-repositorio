const nome = document.getElementById("nome")
const agua = document.getElementById("agua")
const lixo = document.getElementById("lixo")
const posto = document.getElementById("posto")
const submitBtn = document.getElementById("submit-btn")
const resDiv = document.getElementById("res")

submitBtn.addEventListener("click", (e) => {
    e.preventDefault()
    
    const h2 = document.createElement("h2")
    
    resDiv.appendChild(h2)
    

    
    if(nome.value.length == 0 || agua.value.length == 0 || lixo.value.length == 0 || posto.value.length == 0){
         const p = document.createElement("p")
         p.innerText = "Preencha todos os campos"
         resDiv.appendChild(p)
    } else {

        h2.innerText = "--- Resultados e Orientações ---"

        if(agua.value === "sim") {
            const p = document.createElement("p")
            p.innerText = " - Evite descartar medicamentos na água! Isso contamina rios e solos, prejudicando o meio ambiente."
            resDiv.appendChild(p)
        } else {
            const p = document.createElement("p")
            p.innerText = " - Ótimo! Nunca descarte medicamentos na água."
            resDiv.appendChild(p)
        }

        if(lixo.value === "sim") {
            const p = document.createElement("p")
            p.innerText = " - Medicamentos no lixo comum podem causar contaminação. Procure um ponto de coleta autorizado."
            resDiv.appendChild(p)
        } else {
            const p = document.createElement("p")
            p.innerText = " - Excelente! Evitar o lixo comum é uma atitude responsável."
            resDiv.appendChild(p)
        }

        if(posto.value === "não") {
            const p = document.createElement("p")
            p.innerText = " - Informe-se nas farmácias e postos de saúde sobre locais de coleta de medicamentos vencidos."
            resDiv.appendChild(p)
        } else {
            const p = document.createElement("p")
            p.innerText = " - Muito bem! Continue utilizando os pontos de coleta de forma correta."
            resDiv.appendChild(p)
        }

        const span = document.createElement("span")
        resDiv.append(span)
        span.innerText = `Obrigado por participar, ${nome.value}! Sua atitude ajuda a proteger o meio ambiente e a saúde pública.`
        resDiv.style.paddingBottom = "10px"
    }


    
})
