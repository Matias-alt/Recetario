Events();

function Events(){
    document.querySelector('#menuReceta').addEventListener('click', mostrarMenuReceta);
    document.querySelector('#cerrar').addEventListener('click', esconderMenuReceta);
    
    document.querySelector('#eli').addEventListener('click', mostrarConfirmacion);
    document.querySelector('#cancelar').addEventListener('click', esconderConfirmacion);
    
}

function mostrarMenuReceta(e){
    e.preventDefault();

    let menu = document.querySelector('#eliminar');

    menu.classList.add("mostrar");
    menu.classList.remove("esconder");
}

function esconderMenuReceta(e){
    e.preventDefault();

    let menu = document.querySelector('#eliminar');

    menu.classList.add("esconder");
    menu.classList.remove("mostrar");
}

function mostrarConfirmacion(e){
    e.preventDefault();

    let confirmacion = document.querySelector("#confirmar");
    let menu = document.querySelector('#eliminar');

    confirmacion.classList.add("mostrar");
    confirmacion.classList.remove("esconder");
    menu.classList.remove("mostrar");
    menu.classList.add("esconder");
}

function esconderConfirmacion(e){
    e.preventDefault();

    let confirmacion = document.querySelector("#confirmar");

    confirmacion.classList.add("esconder");
    confirmacion.classList.remove("mostrar");
}


