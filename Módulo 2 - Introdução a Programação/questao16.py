# Trocando 'a' por '#'
x = input('Digite uma frase:')
tam = len(x)
for i in range(tam):
        if x[i]=='a' or x[i]=='A':
            print('#', end='')
        else:
            print(x[i], end='')

# Concatenação de String
name = input('Digite seu nome:')
middle = input('Digite seu nome do meio:')
family = input('Digite seu sobrenome:')
completo = name + ' ' + middle + ' ' + family
print(completo)

# Dividindo a frase em palavras
texto = input('Digite uma frase:')
lista = texto.split()
print(lista)
