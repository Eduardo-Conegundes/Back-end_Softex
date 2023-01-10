// Obtém as três notas do aluno
let grade1 = parseFloat(prompt("Informe a nota 1: "));
let grade2 = parseFloat(prompt("Informe a nota 2: "));
let grade3 = parseFloat(prompt("Informe a nota 3: "));

// Calcula a média das três notas
let mean = (grade1 + grade2 + grade3) / 3;

// Utiliza o operador de atribuição para definir a variável "result" como "Aprovado" ou "Reprovado"
let result = mean >= 6 ? "Aprovado" : "Reprovado";

console.log("Média: " + mean);
console.log("Resultado: " + result);
