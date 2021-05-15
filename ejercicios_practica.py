#!/usr/bin/env python
'''
Condicionales [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"


def ej1():
    # Ejercicios de práctica numérica

    # Comparadores
    # Ingrese dos números cualesquiera y realice las sigueintes
    # comparaciones entre ellos
    numero_1 = int(input('Ingrese el primer número:\n'))

    numero_2 = int(input('Ingrese el segundo número:\n'))

    # Compare cual de los dos números es mayor
    # Imprima en pantalla según corresponda
    if numero_1 > numero_2:
        print('numero_1',numero_1 , 'es mayor a numero_2  =', numero_2)
    else:
        print('numero_2',numero_2 , 'es mayor a numero_1  =', numero_1)
    # Verifique si el numero_1 positivo, negativo o cero
    # Imprima el resultado en cada caso
    if numero_1 > 0:
        print('numero 1 es positivo')
    elif numero_1 < 0:
            print('numero 1 es negativo')
    else:
            print('numero 1 es o')
    # Verifique si el numero_1 es mayor a 0 y menor a 100
    # Imprima en pantalla si se cumple o no la condición
    if numero_1 > 0 and numero_1 < 100: 
        print('numero 1 cumple condicion')
    # Verifique si el numero_1 es menor a 10 o el numero_2
    # es mayor a -2
    # Imprima en pantalla si se cumple o no la condición
    if numero_1 < 10 or numero_2 > -2:
        print('cumple')
    else:
            print('no cumple')

def ej2():
    # Ejemplos variables de texto

    # Comparadores
    # Ingrese dos palabras cualesquiera y realice las sigueintes
    # comparaciones entre ellas
    texto_1 = str(input('Ingrese la primera palabra:\n'))

    texto_2 = str(input('Ingrese la segunda palabra:\n'))
    # Compare cual de las dos palabras es mayor (alfabéticamente)
    # Imprima en pantalla según corresponda
    if texto_1 > texto_2:
        print('{} es mayor que {}'.format(texto_1, texto_2))
    else:
        print('{} es mayor que {}'.format(texto_2, texto_1))
    # Compare cual de las dos palabras tiene mayor
    # cantidad de letras
    # Imprima en pantalla según corresponda
    if ((len(texto_1)) > (len(texto_2))):
        print('{} tiene mas letras que {}'.format(texto_1, texto_2))
    else:
        print('{} tiene mas letras que {}'.format (texto_2,texto_1))
    # Verifique si la primera letra de la primera palabra
    # es mayor a la primera letra de la segunda palabra
    # Imprima en pantalla según corresponda
    if texto_1[0] > texto_2[0]:
        print('primer letra de texto 1',texto_1,'es mayor a primer letra de', texto_2)
    else:
        print('primer letra de texto2',texto_2, 'es mayor a primer letra de', texto_1)
    # Copia de la variable texto_1
    copia_texto_1 = texto_1  
    # Verifique que copia_texto_1 es igual a texto_1
    # Imprima en pantalla según corresponda
    # Verifique que copia_texto_1 es distinta a texto_2
    # Imprima en pantalla según corresponda
    if copia_texto_1 == texto_1 and copia_texto_1 != texto_2:
        print('variable texto 1 es igual a 1 ,variable texto 1 no es igual a texto 2')


def ej3():
    # Ejercicios de práctica numérica

    # Condicionales anidados
    numero_1 = 7
    numero_2 = -2

    # Verifique si el numero_1 es mayor a 5
    #   --> En caso afirmativo, verifique si el numero_2
    #       es positivo
    #       --> En caso afirmativo imprima en pantalla "Resp=1"
    #       --> En caso negativo imprima en pantalla   "Resp=2"
    if numero_1 > 5 and numero_2 > 0:
        print ('resp=1')
    else:
        print('resp2')
    #  --> En caso negativo (numero_1 no es mayor a 5)
    #      verifique si el numero_2 es mayor a 5
    #       --> En caso afirmativo imprima en pantalla "Resp=3"
    #       --> En caso negativo imprima en pantalla "Resp=4"
    if not numero_1 > 5 and numero_2 > 5:
        # OJO ACÁ! porque not numero_1 te devuelve "False", te lo pasa a booleano y False siempre va a ser menor a 5 porque es equivalente a cero.
        # en esa línea solo basta con hacer --> if numero_1 < 5  and numero_2 > 5:
        print('resp 3')
    else:
        print('resp 4')

    # Verifique la calificación de un estudiante según su
    # puntaje en un examen
    puntaje = 70
    # Si el puntaje es mayor igual a 90 --> imprimir A
    # Si el puntaje es mayor igual a 80 --> imprimir B
    # Si el puntaje es mayor igual a 70 --> imprimir C
    # Si el puntaje es mayor igual a 60 --> imprimir D
    # Si el puntaje es manor a  60      --> imprimir F
    # Debe imprimir en pantalla la calificacion
    # Utilizar "if" anidados
    if puntaje >= 90:
        print('A')
    if puntaje >= 80:
        print('B')
    if puntaje >= 70:
        print('C')
    if puntaje >= 60 and puntaje < 69:
        print ('D')
    if puntaje < 60:
        print('F')
    # Qué pasa si el puntaje del alumno es 69?
    # Y si es 90 o más, fijate que imprime 'A', 'B' y 'C' porque 90 >= 80 entonces imprime 'B', lo mismo pasa con 'C'
    # Para que no te pase esto tenes que usarlos anidados, es decir, con 'elif' de esa manera va a escapar a los demas condicionales, así:
    
    # puntaje = 91

    # if puntaje >= 90:
    # print('A')
    # elif puntaje >= 80:
    # print('B')
    # elif puntaje >= 70:
    # print('C')
    # elif puntaje >= 60 and puntaje <= 69:
    # print ('D')
    # elif puntaje < 60:
    # print('F')
    

def ej4():
    # Ejemplos variables de texto

    texto_1 = '5'
    texto_2 = '7'
    orden = ['5','7']
    alf = sorted(orden)
    print(alf)


    # Verifique cual cual de los dos textos es mayor alfabéticamente
    # Imprima en pantalla según corresponda

    # Transforma esas variables tipo texto y almacénalas
    # en nuevas variables númericas (int)
    # Repita el proceso, ¿Cuál de las nuevas variables es mayor?
    # Imprima en pantalla según corresponda
    a= texto_1
    b= texto_2
    print(int(texto_1))
    print(int(texto_2))

    # Para pensar!
    # ¿Por qué cree que texto_2 es mayor a texto_1?
    # Siendo números tiene sentido, pero son caracteres, texto,
    # aún así el operador arroja el mismo resultado que con las
    # variables numéricas, cierto? ¿Por qué creen que es así?
    # Esta pregunta estará repetida en el Campus para que puedan
    # responder.
    # NOTA: La respuesta no se encuentra en el apunte, sino en Google ;)

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    #ej1()
    #ej2()
    #ej3()
    ej4()
