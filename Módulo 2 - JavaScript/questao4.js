// Define as variáveis para armazenar os valores
let value1 = parseFloat(prompt("Insira o primeiro valor: "));
let value2 = parseFloat(prompt("Insira o segundo valor: "));

// Obtém o operador aritmético do usuário
let operator = prompt("Insira o operador (+, -, *, /): ");

// Inicializa a variável de resultado
let result;

// Verifica o operador e faz a operação correspondente
switch (operator) {
  case "+":
    result = value1 + value2;
    break;
  case "-":
    result = value1 - value2;
    break;
  case "*":
    result = value1 * value2;
    break;
  case "/":
    result = value1 / value2;
    let remainder = value1 % value2;
    if(remainder > 0) {
        console.log("Resultado: " + result + " Resto : " + remainder);
    }
    else {
        console.log("Resultado: " + result);
    }
    break;
  default:
    console.log("Operador inválido!");
    break;
}

// Se o operador foi válido, exibe o resultado
if (result !== undefined) {
    console.log("Resultado: " + result);
}
