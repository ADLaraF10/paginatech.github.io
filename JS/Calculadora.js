/*-----------------CALCULADORA-----------------------*/

//VARIABLES
let numero1 = "";
let numero2 = "";
let operador = "";
let numero1completo = false;

let expresion = prompt('escriba su expresion simple')

document.write(hacerOperacion(expresion))




//FUNCIONES
function hacerOperacion(expresion){
    datos = getDatos(expresion);
    //console.log(datos.n1 + datos.op + datos.n2 )
    if(datos.op === "+"){
        return datos.n1 + datos.n2; 
    }else if(datos.op === "-"){
        return datos.n1 - datos.n2;
    }else if(datos.op === "*"){
        return datos.n1 * datos.n2;
    }else if(datos.op === "/"){
        return datos.n1 / datos.n2;
    }
    
}

function getDatos(expresion){
    for(i = 0; i < expresion.length ; i++){
        if(expresion[i] != "+" && expresion[i] != "-" && expresion[i] != "*" && expresion[i] != "/"){
            //console.log(expresion[i])
            if(!numero1completo){
                numero1 += expresion[i];
            }else{
                numero2 += expresion[i];
            }
        }else{
            //console.log(expresion[i])
            operador = expresion[i];
            numero1completo = true;
        }
    }
    return dato = { n1: parseInt(numero1), n2:parseInt(numero2), op: operador}
}





