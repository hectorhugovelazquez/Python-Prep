#1: Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
variable=2
print(variable)

#2 Imprimir el tipo de dato de la constante 8.5
b= 8.5
print(type(b))

#3: Imprimir el tipo de dato de la variable creada en el punto 1
print(type(variable))

#4 Crear una variable que contenga tu nombre
nombre= "Hector Hugo Velázquez" 

#5 Crear una variable que contenga un número complejo
complejo= 5 + 5j

#6 Mostrar el tipo de dato de la variable crada en el punto 5
print(type(complejo))

#7 Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
c= 3.1415

#8 Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
variable1= "True"
variable2= True

#9 Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9
print(type(variable1))
print(type(variable2))

#10 Asignar a una variable, la suma de un número entero y otro decimal
suma= 1 + 1.3
print(suma)

#11 Realizar una operación de suma de números complejos
numero= 2 + 5j
numero2= 3 + 8j
operacion= numero + numero2
print(operacion)

#12 Realizar una operación de suma de un número real y otro complejo
a= 4
b= 3 + 5j
c= a+b
print(c)

#13 Realizar una operación de multiplicación
a= 4
b= 6
c= a * b
print(c)




#14 Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15 Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
division= 27/4
print(division)

#16 De la división anterior solamente mostrar la parte entera
print(int(division))

#17 De la división de 27 entre 4 mostrar solamente el resto
resto= 27 % 4
print(resto)

#18 Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
resultado= 6  * 4 + resto
print(resultado)
#19 Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
nombre= "Hector "
apellido= "Velázquez"
print(nombre + apellido)

#20 Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
a= "2" == 2
print(a)


#21 Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
a= int("2") == 2
print(a)

#22 ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
"""a= float("3,8")
print(a)
"""
#23 Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
a= 3
a-=1
print(a)

#24 Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
a= 1 << 2
print(a)

#25 Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
"""No está permitido porque son diferentes tipos de datos"""
#26 Realizar una operación válida entre valores de tipo entero y string
var1= "hola tengo "
var2= 23
var3 = " años"

print(var1 + str(var2) + var3)