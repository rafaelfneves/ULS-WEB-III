#1. Crie um script python que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor

n1 = int(input("Digite o valor de n1: "))
print(f"Numero {n1}, antecessor {n1 - 1}, sucessor {n1 + 1}")

#2. Crie um script python que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
import math
n2 = int(input("\nDigite o valor de n2:"))
dobro=n2*2
print('Dobro {}'.format(dobro))
triplo=n2*3
print('Triplo {}'.format(triplo))
raiz=math.sqrt(n2) 
print('Raiz {}'.format(math.ceil(raiz)))

#3.Crie um script python que leia um valor em metros e a exiba convertido em centimetros e milimetros
n3 = int(input("\nDigite o valor de n3: "))
centimetros=n3*100
milimetros=n3*1000
print('Metros {}, Centimetros {}, Milimetros {}'.format(n3,centimetros,milimetros))

#4. Crie um script python que leia um numero inteiro qualquer e mostre na tela a sua tabuada"""
import random
n4 = random.random()
print(n4)

#5.Crie um script python que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considere a US$1,00=R$4.20"""

#6.Crie um script python que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
#tinta necessária para pinta-la. Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados."""



