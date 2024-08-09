# Exercicios aula Algoritmos Avançados

- ## Exercicio 1  

Canibais e missionários: Três missionários e três canibais vão atravessar de uma margem 
para a outra de um rio, usando um barco onde só cabem duas pessoas de cada vez. Os 
missionários têm que ser cautelosos para que os canibais nunca os excedam em número 
em nenhuma das margens do rio. Como poderão passar todos para a outra margem, 
usando apenas aquele barco? Escreva um algoritmo que demonstre os passos 
necessários para solucionar este problema

passo 1: dois canibais passam  
direita: 2c  
esquerda: 3m x 1c  

passo 2: volta um canibal  
direita: 1c  
esquerda: 3m x 2c  

3: passa 2 canibais  
direita: 3c  
esquerda: 3m x 0c  

4: volta um canibal  
direita: 2c  
esquerda: 3m x 1c  

5: passa 2 missionarios  
direita: 2c x 2m  
esquerda: 1c X 1m  

6: volta um casal  
direita: 1c x 1m  
esquerda: 2c x 2m  

7: passa 2 missionarios  
direita: 1c x 3m  
esquerda: 2c x 0m  

8: volta um canibal  
direita: 0c x 3m  
esquerda: 3c x 0m  

9: passa 2 canibais;  
direita: 2c x 3m  
esquerda: 1c x 0m  

10: volta 1 canibal  
direita: 1c x 3m  
esquerda: 2c x 0m  

11: leva 2 canibais  
direita: 3c x 3m  
esquerda: 0c x 0m  


## Exercicio 2  

Escreva um programa em Python que exiba hello world na tela;  

## Exercicio 3  

Escreva um programa em Python que receba como entrada dois números e retorne a
média aritmética de ambos;

## Exercicio 4  

Reescreva o programa de média aritmética para receber um parâmetro de quantidade
de notas (ex. 5 notas), leia as notas (ex. leia as 5 notas) e retorne a média aritmética
delas. Use um vetor para armazenar as notas. Percorra o vetor para fazer a soma.

## Exercicio 5  

Escreva um programa em Python que calcule o fatorial de um determinado número
informado como parâmetro da sua função. Escreva duas versões desse programa, uma
usando um laço e outra usando recursividade. Dica: fatorial de 5 = 5*4*3*2*1.

## Exercicio 6  

Faça um programa em Python que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que
o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;

## Exercicio 7  

Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em
metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro
para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
em 3 situações:
- Comprar apenas latas de 18 litros;
- Comprar apenas galões de 3,6 litros;
- Misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é,
considere latas cheias.