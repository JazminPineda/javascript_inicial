var combustible = "Diesel";

/* switch sirve para repetir, se coloca la variable que se va a evaluar y enseguida los casos
 cada caso tiene que colocarse la palabra reservada break que especifica que si ya
 a acabado con ese caso no debo continuar
 default es contemplar cualquier caso q no es verdadero en los casos anteriores
 y aparece un anuncado */


switch (combustible) {
    case "Diesel":
        alert("45")
    case "Super97":
        alert("98")
    default:
        alert("no se encuentra en la lista ")
    
}

/*Declarar funcion, no tiene funcion 
Se coloca arriba funciones y se llama abajo */
function miFuncion ( ) {
    alert("este codido esta en la funcion ")
}
miFuncion()