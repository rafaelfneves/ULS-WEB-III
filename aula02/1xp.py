#-*- coding utf-8 -*-
#operadores de comparação >, <, >=,<=, !=, ==

a = 2
b = 4
print('A é maior que B', a>b)
print('B é maior que A', b>a)
print('A é igual a B', a==b)
print('A é diferente de B', a!=b)

n1 = input("Digite um valor de x: ")
print(type(n1))

n2 = input("Digite um valor de y: ")
print(type(n2))

import math #importa todas as funções do math
num=int(input("Digite um numero: "))
raiz=math.sqrt(num) #função squirtle para obter raiz
print('A raiz quadrada de {} é igual a {}'.format(num,math.ceil(raiz))) #math.ceil arredonda para cima

#outra maneira de fazer o import, usando o form

from math import sqrt, floor #importa somente os comandos srqt e o floor
num=int(input('Digite um numero: '))
raiz=math.sqrt(num)
print('A raiz quadrada de {} é igual a {}'.format(num,math.floor(raiz))) #floor arredonda obrigatoriamente para baixo

print("\n=====================================================================\n")


#para gerar numeros aleatorios entre 0 e 1

import random
num1=random.random()
print(num1)

import random
num2=random.randint(1,60)
print(num2)

import random
print(random.randrange(1,20))

print("\n=====================================================================\n")

#Fatiamento de cadeia de caracteres(textos) - Strings

frase=('Aprendendo Python 3 G Falando')
print(frase)
print(frase[4])
print(frase[11:18])
print(frase[11:22:2])
print(frase[:18])
print(frase[8:])
print(frase[::2])

print("\n=====================================================================\n")

#import emoji
#print(emoji.emojize('Python é',use_aliases=True))

#len() - para saber o tamanho de uma string

print('A quantidade de caracteres da frase é: ',len(frase))

#count()- para contar a quantidade de vezes que uma determinada letra se repete
print('A letra A se repete: ',frase.count('a'))

print('A letra A se repete: ',frase.count('a',0,13))

#find()- para saber a posição de uma determinada string

print(frase.find("Python"))

#in para saber se uma determinada string existe
print('Python' in frase)

#replace()-para alterar a palavra na frase, sem alterar a mesma

print(frase.replace('Python', 'PHP'))

frase=('Aula de Python')
frase=frase.replace('Python','PHP')
print(frase)
