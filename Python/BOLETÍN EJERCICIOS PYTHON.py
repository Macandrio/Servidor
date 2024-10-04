#Imprime "Hola, mundo!" en la pantalla. 
print("\nEjercicio 1 ")

print("Hola, Mundo!")

#Calcula la suma de dos números ingresados por el usuario.
print("\nEjercicio 2 ")

num1 = int(input("Ingresa un número entero "))
num2 = int(input("Ingresa un número entero "))
sum = num1 + num2
print("La suma de los numeros es " + str(sum))

#Calcula el área de un triángulo con la fórmula: Área = (base * altura) / 2. 

print("\nEjercicio 3")
base = int(input("Ingresa un número entero "))
altura = int(input("Ingresa un número entero "))

area = (base * altura) / 2

print("El Área del triangulo es: " + str(area))

#Convierte grados Celsius a Fahrenheit
print("\nEjercicio 4")

celsius = float(input("Ingresa un número de grados celsius "))
Fahrenheit = (celsius * 9/5 ) + 32

print("El cambio del es: " + str(Fahrenheit))

#Calcula el factorial de un número.
print("\nEjercicio 5")

num = int(input("Ingresa un número entero "))
sumatorio = 1
for i in range(1, num + 1):
    sumatorio *= i
print("El número total del factorial es: " + str(sumatorio))

#Verifica si un número es par o impar. 
print("\nEjercicio 6")

num = int(input("Ingresa un número entero "))
if num % 2 == 0:
    print("El número " + str(num) + " es par")
else :
    print("El número " + str(num) + " es impar")

#Calcula el máximo común divisor (MCD) de dos números.

print("\nEjercicio 7")

num1 = int(input("Ingresa un número entero "))
num2 = int(input("Ingresa un número entero "))
resultado = 0
a = num1
b = num2
while b != 0:
    a , b = b , a % b
    resultado = a
print("El MCD de " + str(num1) + " y " + str(num2) + " es " + str(resultado))
 
#Imprime los números del 1 al 10 usando un bucle for. 
print("\nEjercicio 8")


for i in range(1, 10 + 1):
    print(i)

#Calcula la suma de los números del 1 al 100. 
print("\nEjercicio 9")
sumatorio = 0

for i in range(1, 11):
    sumatorio += i
print(sumatorio)

#Crea una lista de números y calcula su promedio.
print("\nEjercicio 10")

lista = [5,10,8,20,69]

promedio = sum(lista) / len(lista)  # sum = suma los numeros de la lista
                                    # len = cuenta cuantos elementos hay en la lista
print("El promedio es: " + str(promedio))

#Crea una clase llamada Persona con atributos nombre y edad. Luego, crea un objeto de tipo Persona e imprime sus atributos.
print("\nEjercicio 11")

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_informacion(self):
        print("Nombre: " + str(self.nombre))
        print("Edad: " + str(self.edad))

persona1 = Persona("Juan", 25)
persona1.mostrar_informacion()

#Crea una clase llamada Rectangulo con atributos ancho y altura. Agrega un método para calcular el área del rectángulo y otro para calcular su perímetro
print("\nEjercicio 12")


class Rectangulo:
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    def calcular_area(self):
        return self.ancho * self.altura
    
    def calcular_perimetro(self):
        return 2 * (self.ancho + self.altura)
    
rectangulo1 = Rectangulo(5, 10)

print("Área: " + str(rectangulo1.calcular_area()))
print("Perímetro: " + str(rectangulo1.calcular_perimetro()))

#Crea una clase llamada Estudiante con atributos nombre, edad y curso. Crea varios objetos de tipo Estudiante y almacénalos en una lista.
#Luego, itera sobre la lista e imprime la información de cada estudiante. 
print("\nEjercicio 13")

class Estudiante:
    
    def __init__(self, nombre, edad, curso):
        self.nombre = nombre
        self.edad = edad
        self.curso = curso

    
    def mostrar_informacion(self):
        print("Nombre: " + self.nombre + ", Edad: " + str(self.edad) + ", Curso: " + self.curso)




estudiante1 = Estudiante("Ana", 20, "Matemáticas")
estudiante2 = Estudiante("Luis", 22, "Física")
estudiante3 = Estudiante("María", 21, "Química")

lista_estudiantes = []

lista_estudiantes.append(estudiante1)
lista_estudiantes.append(estudiante2)
lista_estudiantes.append(estudiante3)


for estudiante in lista_estudiantes:
    estudiante.mostrar_informacion()


#Crea una clase llamada CuentaBancaria con atributos titular y saldo. Agrega métodos para depositar y retirar dinero de la cuenta. 
print("\nEjercicio 14")

class CuentaBancaria:

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo


    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(self.titular + " depositó " + str(cantidad) + ". Nuevo saldo: " + str(self.saldo))
        else:
            print("La cantidad a depositar debe ser positiva.")


    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                print(self.titular + " retiró " + str(cantidad) + ". Nuevo saldo: " + str(self.saldo))
            else:
                print("Fondos insuficientes.")
        else:
            print("La cantidad a retirar debe ser positiva.")

cuenta1 = CuentaBancaria("Juan", 500)

cuenta1.depositar(200)
cuenta1.retirar(100)
cuenta1.retirar(700)


#Crea una clase llamada Coche con atributos marca y modelo. Crea un método que imprima la información del coche en un formato legible. 
print("\nEjercicio 15")

class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


    def mostrar_informacion(self):
        print("Marca: " + self.marca + ", Modelo: " + self.modelo)

coche1 = Coche("Toyota", "Corolla")
coche1.mostrar_informacion()

#Crea una clase base llamada Animal con un método hablar que imprima un mensaje genérico. 
#Luego, crea dos clases derivadas, Perro y Gato, que hereden de Animal y sobrescriban el método hablar para imprimir mensajes diferentes. 
print("\nEjercicio 16")


class Animal:

    def hablar(self):
        print("Este animal hace un sonido.")


class Perro(Animal):

    def hablar(self):
        print("El perro ladra.")


class Gato(Animal):

    def hablar(self):
        print("El gato maulla.")


mi_perro = Perro()
mi_gato = Gato()

mi_perro.hablar()  
mi_gato.hablar() 

#Crea una clase base llamada FiguraGeometrica con atributos ancho y altura, y un método area que calcule el área de la figura. 
#Luego, crea clases derivadas como Rectangulo y Triangulo que hereden de FiguraGeometrica y sobrescriban el método area para calcular el área específica de cada figura.
print("\nEjercicio 17")


class FiguraGeometrica:
    
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura

    
    def area(self):
        return 0  


class Rectangulo(FiguraGeometrica):

    def area(self):
        return self.ancho * self.altura


class Triangulo(FiguraGeometrica):
    
    def area(self):
        return (self.ancho * self.altura) / 2

rectangulo = Rectangulo(5, 10)
triangulo = Triangulo(5, 10)

print("Área del rectángulo: " + str(rectangulo.area()))  
print("Área del triángulo: " + str(triangulo.area())) 

#Crea una clase base llamada Vehiculo con atributos marca y modelo, y un método informacion que imprima la información del vehículo.
#Luego, crea clases derivadas como Coche y Bicicleta que hereden de Vehiculo y añadan atributos y métodos específicos de cada tipo de vehículo.
print("\nEjercicio 18")


class Vehiculo:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def informacion(self):
        print("Marca: " + self.marca + ", Modelo: " + self.modelo)

class Coche(Vehiculo):

    def __init__(self, marca, modelo, tipo_combustible):
        super().__init__(marca, modelo)  
        self.tipo_combustible = tipo_combustible


    def informacion(self):
        super().informacion()  
        print("Tipo de combustible: " + self.tipo_combustible)

class Bicicleta(Vehiculo):
    
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)  
        self.tipo = tipo


    def informacion(self):
        super().informacion()  
        print("Tipo de bicicleta: " + self.tipo)

coche1 = Coche("Toyota", "Corolla", "Gasolina")
bicicleta1 = Bicicleta("Giant", "Escape 3", "Urbana")

print("Información del coche:")
coche1.informacion()
print("\nInformación de la bicicleta:")
bicicleta1.informacion()

#Crea una clase base llamada InstrumentoMusical con un método tocar que imprima un mensaje genérico. 
#Luego, crea clases derivadas como Piano y Guitarra que hereden de InstrumentoMusical y sobrescriban el método tocar para imprimir mensajes diferentes.
print("\nEjercicio 19")


class InstrumentoMusical:

    def tocar(self):
        print("Este instrumento está sonando.")

class Piano(InstrumentoMusical):

    def tocar(self):
        print("El piano está tocando una melodía suave.")

class Guitarra(InstrumentoMusical):

    def tocar(self):
        print("La guitarra está tocando acordes vibrantes.")

piano1 = Piano()
guitarra1 = Guitarra()

piano1.tocar()
guitarra1.tocar()

#Crea una clase base llamada Empleado con atributos nombre y salario, y un método calcular_salario_anual que calcule el salario anual del empleado.
#Luego, crea clases derivadas como Gerente y Programador que hereden de Empleado y añadan atributos y métodos específicos de cada tipo de empleado.
print("\nEjercicio 20")

class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

    def calcular_salario_anual(self):
        return self.salario * 12

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)
        self.departamento = departamento

    def informacion(self):
        return "Nombre: " + self.nombre + ", Salario Anual: " + str(self.calcular_salario_anual()) + ", Departamento: " + self.departamento

class Programador(Empleado):
    def __init__(self, nombre, salario, lenguaje):
        super().__init__(nombre, salario)
        self.lenguaje = lenguaje

    def informacion(self):
        return "Nombre: " + self.nombre + ", Salario Anual: " + str(self.calcular_salario_anual()) + ", Lenguaje: " + self.lenguaje

gerente1 = Gerente("Laura", 5000, "Ventas")
programador1 = Programador("Carlos", 4000, "Python")

print(gerente1.informacion())
print(programador1.informacion())
