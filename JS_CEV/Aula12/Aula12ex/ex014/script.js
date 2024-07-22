function carregar(){
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data =new Date()
    var hora=data.getHours()
    
    var minutos= data.getMinutes()
    if (minutos<10){
        minutos = "0"+minutos
    }
    
    msg.innerHTML= `Agora são ${hora}:${minutos} horas.`
    if (hora >= 0 && hora < 12){
        //bom dia
        img.src = 'fotomanha2.png'
        document.body.style.background = '#e2cd9f'
    } else if (hora >= 12 && hora <= 18){
        //boa tarde
        img.src = 'fototarde2.png'
        document.body.style.background = '#b9846f'
    }else{
        //boa noite
        img.src = 'fotonoite2.png'
        document.body.style.background = '#515154'
    }


}
