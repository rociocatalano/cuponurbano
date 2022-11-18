/*function view() {
    let nombre = document.getElementById("nombre");
    let apellido = document.getElementById("apellido");
    let dni = document.getElementById("dni");
    let alias = document.getElementById("alias");
    let contrasenia = document.getElementById("contrasenia");
    let email = document.getElementById("email");

    var myModal = new bootstrap.Modal(document.getElementById('modal'), {
        keyboard: false
    })
    myModal.show();
}*/

function mostrarDatos() {
    let nombre = document.getElementById("nombre");
    let apellido = document.getElementById("apellido");
    let dni = document.getElementById("dni");
    let alias = document.getElementById("alias");
    let contrasenia = document.getElementById("contrasenia");
    let email = document.getElementById("email");
    let estado = true;

    if (nombre.value == '') {
        modalMostrar('Falta completar el campo "nombre"', 'Debe completar el campo "nombre" para continuar');
        estado = false;
    } else if (apellido.value == '') {
        modalMostrar('Falta completar el campo "apellido"', 'Debe completar el campo "apellido" para continuar');
        estado = false;
    } else if (dni.value == '') {
        modalMostrar('Falta completar el campo "DNI"', 'Debe completar el campo "DNI" para continuar');
        estado = false;
    } else if (!Number.isInteger(parseInt(dni.value))) {
        modalMostrar('Valor incorrecto', 'El campo "DNI" solo puede incluir números');
        estado = false;
    } else if (alias.value == '') {
        modalMostrar('Falta completar el campo "Alias"', 'Debe completar el campo "Alias" para continuar');
        estado = false;
    } else if (contrasenia.value == '') {
        modalMostrar('Falta completar el campo "Contraseña"', 'Debe completar el campo "Contraseña" para continuar');
        estado = false;
    } else if (email.value == '') {
        modalMostrar('Falta completar el campo "E-mail"', 'Debe completar el campo "E-mail" para continuar');
        estado = false;
    }
    /*
        if (estado == true) {
            modalMostrarDatos("¡Atención!", "¿Comprobó que todos los datos sean correctos?")

        }*/

}

function modalMostrar(titulo, descripcion) {
    let tituloElemento = document.getElementById('modal-title');
    let textoElemento = document.getElementById('modal-body');

    tituloElemento.innerHTML = titulo;
    textoElemento.innerHTML = descripcion;

    var myModal = new bootstrap.Modal(document.getElementById('modal'), {
        keyboard: false
    })
    myModal.show();
}

function cerrar() {
    $("#exampleModal").modal('hide'); //ocultamos el modal
    $('body').removeClass('modal-open'); //eliminamos la clase del body para poder hacer scroll
    $('.modal-backdrop').remove(); //eliminamos el backdrop del modal

}

function valideKey(evt) {
    var code = (evt.which) ? evt.which : evt.keyCode;

    if (code == 8) { // backspace.
        return true;
    } else if (code >= 48 && code <= 57) { // is a number.
        return true;
    } else { // other keys.
        return false;
    }
}