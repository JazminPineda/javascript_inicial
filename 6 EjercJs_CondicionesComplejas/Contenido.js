var balance = 50000;
if (balance >= 0){
    alert("El balance es positivo")
    if(balance < 100000) { // estructura de control anidado
        alert("El balance es menor que 100.000")
    }
} else{
    alert("El balance es negativo")
}