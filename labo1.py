#!/usr/bin/python3
altura= int(input('Ingrese la cantidad de iteraciones '))
caracter= input('Ingrese el caracter deseado ')

for x in range(altura,0,-1):
    for j in range (0,x,1):
        print(caracter,end="")
    print(" ")


