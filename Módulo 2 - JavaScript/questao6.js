// função tradicional sem parâmetros
function imprimirMensagem() {
    console.log("Calculadora iniciada!");
}

// função tradicional com parâmetros e retorno
function somar(a, b) {
    return a + b;
}

// arrow function com parâmetros e retorno
const multiplicar = (a, b) => {
    return a * b;
}

// Utilizando as funções
imprimirMensagem();
console.log("5 + 2 = " + somar(5, 2));
console.log("5 x 3 = " + multiplicar(5, 3));
