#DHacer un pequeño tutorial en un Google Dosc de cada una de las funciones de debug con VsCode.
#Hacer el ejemplo con una un programa que tenga 4 funciones : sumar, restar, multiplicar y dividir.
#Explicar el panel dónde se ven las variable locales y globales.

def sumar(a , b):
    suma = a + b
    return suma

def restar(a , b):
    resta = a - b
    return resta

def dividir(a , b):
    div = a / b
    return div

def mult(a , b):
    mul = a * b
    return mul

num1 = int(input("Escribe un numero "))
num2 = int(input("Escribe un numero "))

ressuma = sumar(num1,num2)
resres = restar(num1,num2)
resdiv = dividir(num1,num2)
resmul = mult(num1,num2)


print("La suma es : " + str(ressuma) + " La resta es: " + str(resres) + " La dividion es: " + str(resdiv) + "La multiplicacion es: " + str(resmul))


