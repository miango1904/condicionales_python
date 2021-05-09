#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos adquiridos durante la semana
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.3"


def ej1():
    print('Ejercicios de práctica con números')
    '''
    Realice un programa que solicite por consola 2 números
    Calcule la diferencia entre ellos e informe por pantalla
    si el resultado es positivo, negativo o cero.
    '''
    pri_num = int(input('Ingrese el primer número:\n'))
    seg_num = int(input('Ingrese el segundo número:\n'))
    dif_num = pri_num - seg_num
    if dif_num > 0 :
        print('el resultado de la diferencia es positivo :',dif_num)
    elif dif_num < 0 :
        print('el resultado de la diferencia es negativo :', dif_num)
    else:
        print('el resultado es cero', dif_num) 


def ej2():
    print('Ejercicios de práctica con números')
    '''
    Realice un programa que solicite el ingreso de tres números
    enteros, y luego en cada caso informe si el número es par
    o impar.
    Para cada caso imprimir el resultado en pantalla.
    '''
    pri_num = int(input('Ingrese el primer número:\n'))
    seg_num = int(input('Ingrese el segundo número:\n'))
    ter_num = int(input('Ingrese el tercer número:\n'))
    if pri_num %2 == 0:
        print('el primer numero es par')
    elif pri_num % 2 !=0:
        print('primer numero no es par')
    
    if seg_num %2 == 0:
        print('el segundo numero es par')
    elif pri_num % 2 !=0:
        print('segundo numero no es par')

    if ter_num %2 == 0:
        print('el tercer numero es par')
    elif ter_num % 2 !=0:
        print('tercer numero no es par')
    
    


def ej3():
    print('Ejercicios de práctica con números')
    '''
    Realice una calculadora, se ingresará por línea de comando dos números
    Luego se ingresará como tercera entrada al programa el símbolo de la operación
    que se desea ejecutar
    - Suma (+)
    - Resta (-)
    - Multiplicación (*)
    - División (/)
    - Exponente/Potencia (**)
    Se debe efectuar el cálculo correcto según la operación ingresada por consola
    Imprimir en pantalla la operación realizada y el resultado
    '''
    pri_num = int(input('Ingrese el primer número:\n'))
    seg_num = int(input('Ingrese el segundo número:\n')) 
    Suma = 1
    Resta = 2
    Multiplicación = 3
    División = 4
    Potencia =  5
    operador = int(input('Ingrese el numero del operador deseado\n'))
    if operador == 1:
        print(pri_num + seg_num)
    if operador == 2:
        print(pri_num - seg_num)
    if operador == 3 :
        print(pri_num * seg_num)
    if operador == 4 :
        print(pri_num / seg_num)
    if operador == 5:
        print(pri_num ** seg_num)



def ej4():
    print('Ejercicios de práctica con cadenas')

    '''
    Realice un programa que solicite por consola 3 palabras cualesquiera
    Luego el programa debe consultar al usuario como quiere ordenar las palabras
    1 - Ordenar por orden alfabético (usando el operador ">")
    2 - Ordenar por cantidad de letras (longitud de la palabra)

    Si se ingresa "1" por consola se deben ordenar las 3 palabras por orden alfabético
    e imprimir en pantalla de la mayor a la menor

    Si se ingresa "2" por consola se deben ordenar las 3 palabras por cantidad de letras
    e imprimir en pantalla de la mayor a la menor
    '''
    palab_1 = (input('Ingrese primer palabra:\n'))
    palab_2 = (input('Ingrese segunda palara:\n'))
    palab_3 = (input('Ingrese tercer palabra:\n'))
    lista = [palab_1,palab_2,palab_3]
    lista.sort()
    
    orden = int(input('Ingrese el número de orden deseado alfabetico:1,longitud:2:\n'))
    if orden == 1:
        print (lista)
    if orden == 2:
        print (sorted(lista, key=len))



def ej5():
    print('Ejercicios de práctica con números')

    '''
    Realice un programa que solicite ingresar tres valores de temperatura
    De las temperaturas ingresadas por consola determinar:
    1 - ¿Cuáles de ellas es la máxima temperatura ingresada?
    2 - ¿Cuáles de ellas es la mínima temperatura ingresada?
    3 - ¿Cuál es el promedio de las temperaturas ingresadas?

    En cada caso imprimir en pantalla el resultado
    '''
    pri_num = int(input('Ingrese el primer número:\n'))
    seg_num = int(input('Ingrese el segundo número:\n'))
    terc_num = int(input('Ingrese el tercer número:\n'))
    promedio = (pri_num + seg_num + terc_num) / 3
    if pri_num > seg_num and pri_num> terc_num:
        print('el valor maximo es :' , pri_num)
    elif seg_num > pri_num and pri_num > terc_num:
        print('el valor maximo es :',seg_num)
    elif terc_num > seg_num and terc_num> pri_num:
        print('el valor maximo es :',terc_num)

    if pri_num < seg_num and pri_num<terc_num:
        print(' el valor minimo es : ',pri_num)
    elif seg_num < pri_num and pri_num < terc_num:
        print(' el valor minimo es : ',seg_num)
    elif terc_num < seg_num and terc_num< pri_num:
        print(' el valor minimo es : ',terc_num)
    print('el promedio obtenido es :', promedio)

if __name__ == '__main__':
    print("Ejercicios de práctica")
    #ej1()
    #ej2()
    #ej3()
    #ej4()
    #ej5()
