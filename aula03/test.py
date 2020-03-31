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