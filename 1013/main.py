# -*- coding: utf-8 -*-

'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''

A, B, C = map(int, input().split())

maiorAB = (A + B + abs(A - B)) / 2

maiorABC = (maiorAB + C + abs(maiorAB - C)) / 2

maiorABC = int(maiorABC)

print(f'{maiorABC} eh o maior')