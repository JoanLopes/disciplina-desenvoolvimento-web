function alertClient(){
    alert('falei para nao clicar!')
}

function gerarMsg() {
    let mensagens = [
        "Essa é a mensagem 1.",
        "Esta é a mensagem 2.",
        "Aqui está a mensagem 3.",
        "Mensagem aleatória 4.",
        "Uma mensagem diferente 5."
    ];

    let indice = Math.floor(Math.random() * mensagens.length);
    let div = document.getElementById("gerar-msg");
    div.innerHTML = mensagens[indice];
}