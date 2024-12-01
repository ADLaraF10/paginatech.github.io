
/* SMOOTH SCROLLING */
const enlaces = document.querySelectorAll("nav a");

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

