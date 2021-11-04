#!/usr/bin/phyton3

#Carlos Smith Ulloa B36684

#variable en la que guardaremos los nombres.

lista_nombres=[]

#Condicción de ejecución del programa

while(True):
    name=input('Escriba un nombre, o SALIR para salir: ')
    if(name=='SALIR'):break 
    _nombre=name.lower()

    #Separamos el nombre y apellidos en una tupla.
    nombretupla=_nombre.split(" ")
    
    #Validamos el Nombre entregado.
    if all(name.isalpha() or name.isspace() for name in nombretupla):

        #leemos el número de elementos entregados.
        num_nombres=len(nombretupla)
        
        #Cuando son 3 elementos.
        if(num_nombres==3):
            nombre=nombretupla[0]
            apellido1=nombretupla[1]
            apellido2=nombretupla[2]
            x= True

        #Cuando son 4 elementos.
        elif(num_nombres==4):
            nombre=nombretupla[0]+" "+nombretupla[1]
            apellido1=nombretupla[2]
            apellido2=nombretupla[3]
            x= True
    
        else:
            print('Debe ingresar sólo 3 o 4 elementos ')  
            x= False
    else:
        print('Debe ingresar sólo caracteres')
        x= False

    #Damos Forma a lo encontrado.
    if(x==True):
        nombre=nombre.title()
        apellido1=apellido1.capitalize()
        apellido2=apellido2.capitalize()
    
        #Agregamos todo en una nueva cadena de texto.
        nombre_completo=nombre+" "+apellido1+" "+apellido2

        #Integramos todos los nombres en una lista.
        lista_nombres.append(nombre_completo)

#Utilizamos un for para imprimir cada nombre en lista.

for element in lista_nombres:
    print(element)

