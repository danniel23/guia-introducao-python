# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.

a, b, c = map(int, input().split())
soma = a + b + c
mult= a*b*c
div= soma/ 2
print(soma)
print(mult)
print(div)

# Escreva um programa que leia um número e apresente a raiz quadrada deste número.

x = int(input("Entre  a number: "))
raiz= ((x)**(1/2))
print(raiz)


