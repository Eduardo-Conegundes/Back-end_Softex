// Obtém as duas notas do aluno
let grade1 = parseFloat(prompt("Informe a nota 1: "));
let grade2 = parseFloat(prompt("Informe a nota 2: "));

// Calcula a média das duas notas
let mean = (grade1 + grade2) / 2;

// Calcula a nota mínima que o aluno deve tirar na próxima prova para passar com nota 7
let min_grade = 7 * 3 - mean * 2;

console.log("Nota mínima para passar com 7: " + min_grade.toFixed(2));
