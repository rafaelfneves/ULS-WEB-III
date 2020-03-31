# -*- coding: utf-8 -*-
print('==============================[Q1]==============================')
#1.Crie um script python que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

valor = float(input('Digite o valor do produto'))
porcentagem = (valor/100)*5

valor = valor - porcentagem
print("{} ".format(valor))

print('==============================[Q2]==============================')
#2.Crie um script python que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salario=float(input("\nQual o seu salario? "))

novoSal=(salario * 0.15) + salario 

print('Seu salario com o  bonus será de: {}'.format(novoSal))

print('==============================[Q3]==============================')
#3.Crie um script python que converta uma temperatura digitada em graus Celsius para Fahrenheit.
celsius = float(input('Digite o valor em celsius'))

farenheit = (celsius * 9/5) + 32 



print("{} graus em farenheit".format(farenheit))

print('==============================[Q4]==============================')
#4.Crie um script python que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por KM rodado.

KmQ4=float(input("\nQuantos quilometros percorridos? "))
diasQ4=int(input("\nQuantos dias alugado? "))

precoKmQ4 = 0.15 * KmQ4
precoDiasQ4 = 60 * diasQ4
precoTotalQ4 = precoKmQ4 + precoDiasQ4

print('O total a pagar será de: {}'.format(precoTotalQ4))

print('==============================[Q6]==============================')
#6.Crie um programa que leia o nome completo de uma pessoa e mostre:
#a)O nome com todas as letras maiúsculas e minúsculas
#b)Quantas letras ao todo(sem considerar espaços)
#c)Quantas letras tem o primeiro nome

nome = input('Digite seu nome')

print(nome.upper())

print(nome.lower())

print('{}'.format(len(nome.strip())))

print('{}'.format(nome[0], len(nome[0])))

print('==============================[Q7]==============================')
#7. Faça um program que leia um numero de 0 a 9999 e mostre na tela cada um dos dígitos separadamente.
#exemplo:unidade: 4 dezena: 3 centena: 8 milhar

numero = float(input('Digite um numero ate 9999: '))

if numero < 100 :
    print('Dezena')

if numero > 999 :
   print('milhar')

if numero < 1000 and numero > 99:
   print('centena')

print('{}'.format(numero))

print('==============================[Q8]==============================')
#8.Escreva um programa que faça o computador "pensar" em um numero inteiro 
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o numero escolhido 
#pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
alQ8=(randint(0,5))

respQ8=int(input('Advinhe o número de 0 a 5: '))

if respQ8 == alQ8:
    print('Venceu!')
else:
    print('Perdeu!')

print('==============================[Q9]==============================')
#9.Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada KM acima do limite.

varQ9 = int(input('Digite a velocidade do carro em Km/h: '))

if varQ9 > 80:
    varQ9 -= 80
    custoQ9 = varQ9 * 7
    print('Você foi multado! multa de: R${}'.format(custoQ9))

print('==============================[Q10]==============================') 
#10.Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
#KM para viagens de até 200Km e R$0,45 para viagens mais longos.

viagem = float(input("Digite a distancia viajada em km: "))

if viagem < 200 :
    passagem = viagem * 0.50

if viagem > 200 :
    passagem = viagem * 0.45

print('Valor foi de {}'.format(passagem))

print('==============================[Q11]==============================')
#11.Faça um programa que leia um ano qualquer e mostre se ele é Bissexto.

varQ11=int(input('Digite um ano: '))

if varQ11 % 4 == 0:
    print('Ele é Bissexto')
else:
    print('Não é Bissexto')

print('==============================[Q12]==============================')
#12.Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

primeiro=int(input('Digite o primeiro numero: '))
segundo=int(input('Digite o segundo numero: '))
terceiro=int(input('Digite o terceiro numero: '))

maior = primeiro
menor = primeiro

if segundo > maior:
        maior = segundo

if terceiro > maior:
        maior = terceiro

print('Maior: {}'.format(maior))

if segundo < menor:
    menor = segundo

if terceiro < menor:
    menor = terceiro

print('Menor: {}'.format(menor))

print('==============================[Q13]==============================')
#13.Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores
#a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o numero é de 15%.

salario = float(input('Digite o valor do salario: '))

if salario > 1250 :
    salario = (salario10)/100 + salario
if salario < 1250 :
    salario =(salario15)/100  + salario

print('Salario aumentado foi de {}'.format(salario))

print('==============================[Q14]==============================')
#14.Escreva um programa que leia o comprimento de 3 retas e diga ao usuário se ela podem ou não formar um triângulo.

lado1 = float(input('Digite o tamanho da primeira linha: '))
lado2 =  float(input('Digite o tamanho da segunda linha: '))
lado3 = float(input('Digite o tamanho da terceira linha: '))

if lado1 < lado2 + lado3 and lado2 < lado1+lado3 and lado3 < lado1 + lado2 :
   print('podem formar um triangulo')
else :
    print('Não podem formar um triangulo')