# -*- coding: utf-8 -*-
print('==============================[INICIO]==============================')

#String
frase=('Aula Online')

#upper() - para colocar em letra maiuscula

print(frase.upper())

print(frase.upper().count('O'))

#lower() - para colocar em letra minúscula

print(frase.lower())

#capitalize() 
print(frase.capitalize())

#title() - vai analisar quantas palavras tem essa string, e transformar todas as primeiras letras de cada palavra

print(frase.title())

#swapcase() - inverte a caixa da string, o que é maiusculo vira minusculo e vice versa

print(frase.swapcase())

#strip() - remove os espaços

print(frase.strip())

#rstrip() - Remove espaço do lado direito

print(frase.rstrip())

#rstrip() - Remove espaço do lado esquerda

print(frase.lstrip())

#split() - dividir em sub strings, uma função que retorna uma lista

print(frase.split())

#join() - para definir o separador da palavra

print('-'.join(frase))

#===formatação de string===
#center() - centralizar

print(frase.center(100))
print(frase.center(100,'*'))

#ljust() - para alinhar a esquerda

print(frase.ljust(100))
print(frase.ljust(100,'-'))

#rjust() - para alinhar a direita

print(frase.rjust(100))
print(frase.rjust(100,'&'))

#Estruturas Condicionais - simples(if); composta(else); aninhada(elif)

a=7
b=9

if a>b:
    print('A variavel A é maior: {}'.format(a))
if a<b:
    print('A variavel B é maior: {}'.format(b))

#tipo um scanf
nome=input("\nQual o seu nome?")

if nome=='Rafael':
    print('Esse nome é maravilhoso')

print('Bom dia!!{}'.format(nome))    

#Exemplo de condicional composta

ano=int(input('\nQuantos anos tem o seu carro?'))
if ano <= 5:
    print('Carro Novo')
else :
    print('Carro Velho')


n1= float(input('Digite a nota 1: '))
n2= float(input('Digite a nota 2: '))

media = n1+n2/2

if media >= 7:
    print('Passou!')
else:
    print('Reprovou!')

#Indicar se o numero digitado é par ou impar

print('================================[FIM]================================')