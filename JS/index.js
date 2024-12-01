
/* SMOOTH SCROLLING */
const enlaces = document.querySelectorAll(".referencia");

enlaces.forEach(enlace => {
    console.log("hola");
    enlace.addEventListener("click", evento => {
        evento.preventDefault()

        const idDestino = enlace.getAttribute("href").slice(1);
        const objDestino = document.getElementById(idDestino);

        console.log(idDestino);

        objDestino.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });
    });
});

/* VALIDAR FORMULARIO */

function validarFormularioMensaje(event) {
    event.preventDefault()
    const campos = document.querySelectorAll('#seccion_form input[type="text"],textArea'); 
    console.log(campos);
    let camposVacios = false;
    campos.forEach(campo => {
      console.log("Revisando campo...");
      const span = document.getElementById('alerta');
      if (campo.value.trim() === "") {
        span.style.display = 'inline'
        camposVacios = true;
      }else{
        span.style.display = 'none'
      }

      return camposVacios;
    });
}

