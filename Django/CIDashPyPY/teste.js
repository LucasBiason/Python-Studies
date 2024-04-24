function pares(x, y){
    console.log(" 1ª Forma ")
    // 1ª Forma: 1 em 1 verificando (a mais simples, porem consome mais memoria e processamento)
    for (var n = x; n <= y; n++){
        if (n % 2 == 0){
            console.log(n)
         }
    }

    console.log(" 2ª Forma ")
    // 2º Forma: 2 em 2 (mais complexa, metade do processamento)
    // preciso definir um numero inicial que vai de 2 em 2
    var initial_number = x; // Assumo que X eh par
    // verifica se X eh impar 
    if (x % 2 != 0){
        initial_number = x + 1
    }
    // Com isso eu vou de 2 em dois com o numeros
    console.log(n)
    for (var n = initial_number; n < y; n=n+2){
        console.log(n)
    }
}

pares(32,321)