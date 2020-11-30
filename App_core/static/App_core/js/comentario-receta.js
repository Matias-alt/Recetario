function Events(){
    document.querySelector('#comment').addEventListener('click', EfectoLikeComentario);
}

function EfectoLikeComentario(e){
    e.preventDefault();

    console.log('ok');
}

Events();