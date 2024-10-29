# entrega_de_trabajos
Mi pagina web va a consistir en un Aeropuerto en general con sus aerolineas que serian las distintas empresa como rayane, vueling ... ,
los vuelos que hay con sus pasajeros que seran las personas , los trabajadores que trabajen en el aeropuerto , el equipage que lleve una persona tambien las reservas de las personas , las ruta que deben tomar los aviones, y lod sitios del avion donde se sienta la gente.

sera una pagina donde se controlara toda la informacion de un aeropuerto 
-------------------------------------------------------------------------------------------------------------------------------------------
Aeropuerto
    Atributos: 4
        Nombre (varchar ,maximo de caracteres 100, Definimos el nombre de la tabla admin)
        Ciudad (varchar ,maximo de caracteres 2, choices para que solo pueda elegir entre varias ciudades , por defecto que ponga ES)
        País (varchar , maximo de caracteres 2, choices para que solo pueda elegir entre varios paises , por defecto que ponga ES)
        capacidad maxima (Entero, este campo por defecto es 150 aviones)

        Funcion:
            str: para que en el admi aparezca el nombre

ContactoAeropuerto
    Atributos: 4
        nombre_contacto (varchar , maximo caracteres 100)
        telefono_contacto (varchar , maximo caracteres 100)
        email_contacto(email , se puede dejar en blanco)
        años_trabajado (Entero, el nombre se pone años trabajo , por defecto 0 años)
        
        Relacion: 
            Aeropuerto(OneToOne)

        Funcion: 
            str: Devuelve el nombre del contacto en el admin f para concadenar

Aerolinea
    Atributos: 4
        nombre (varchar de 100 caracterex max, nombre que mostrara en el formulario en vez de nombre aerolinea operadora)
        codigo (varchar, maximo 10 caracteres)
        fecha_fundacion (dia y hora , guarda automaticamente la fecha y hora al crear un registro)
        pais (varchar, maximo 2 caracteres , chices para que elija uno de los paises proporcionados, por defecto sera españa)

        Relacion : 1
            aerolinea(ManyToMany)
        
        Funcion: 
            str: Devuelve el nombre en el admin


Vuelo
    Atributos: 5
        hora_salida (dia y hora , no se puede dejar en blanco y sae un mensaje de error)
        hora_llegada (dia y hora , no se puede dejar en blanco y sae un mensaje de error)
        estado (si esta volando o no , nombre de la columna en la base de datos Volando)
        duracion(duracion , no se puede editar)

        Relacion:
            origen (ManyToOne)
            destino (ManyToOne)
            aerolinea (ManyToMany)

        Funcion:
            Clean => Verifica que el aeropuerto destino y origen no coincida
            save => calcula la duracion del vuelo

EstadisticasVuelo
    Atributos: 
        fecha_estadisticas (Dato , se pone automaticamente la fecha de creacion si no pones nada)
        numero_asientos_vendidos = (Entero, por defecto 0)
        numero_cancelaciones(Enteros , por defecto 0)
        feedback_pasajeros (varchar , se puede dejar en blanco)

        Relacion:
            Vuelo(OneToOne)


Pasajero
    Atributos: 5
        nombre (varchar,maximo 20 caracteres)
        apellido (varchar, maximo 20 caracteres, hacepta valores vacios)
        email (verifica el correo)
        telefono (Enteros , valida hasta 9 valores, puede ser un campo vacio)
        fecha de nacimiento (Dia y hora, puede ser nulo)

        Relacion:2
            Vuelo(ManyToMany)

        Funcion:
            str: muestra el nombre y apellido en el admin
            Valida si el dominio esta bien o no escrito y te pone un erro si no esta bien escrito

PerfilPasajero
    Atributos:
        direccion (varchar , maximo de caracteres 255, se puede dejar en blanco)
        documento_identidad (varchar , maximo de caracteres 9, es unico no puede a ver mas de uno)
        nacionalidad (varchar , maximo de caracteres 50, se puede dejar en blanco)
        vivienda (varchar , maximo de caracteres 50, se puede dejar en blanco)
        Relaciones:
            pasajero (OneToOne)

        Funcion
            str (muestra Dni en el admin)

Equipage
    Atributos: 4
        peso (decimales)
        dimensiones (varchar maximo 100 caracteres)
        tipo de material (varchar),maximo 100 caracteres
        color (varchar)

        Relacion: 2
            pasajero (ManyToOne)

        Funcion:
            str (muestra en el admi una cadena)


VueloAerolinea (Tabla intermedia)
    Atributos: 5
        fecha operacion(dia y hora, se puede poner nulo)
        esatdo (texto)
        clase(varchar , choices para elegir una clase)
        numero de aviones volando (Enteros,por defecto 5)
        insidencias (varchar , maximo caracteres 100)
        Relaciones: 2
            vuelo(ManyToOne)
            aerolinea(ManyToOne)

Reserva
    Atributo
        fecha de la reserva (por defecto es la fechqa de creacion)
        estado (varchar maximo 50 caracteres, introduce una ayuda)
        metodo de pago (varchar, choise para elegir metodo, por defecto targeta)
        codigo de descuento (varchar de 100 caracteres)

        Relacion
            pasajero(ManyToOne)
            vuelo(ManyToOne)

Asiento
    Atributos
        clase (varchar , maximo 1 caracter, choices para elegir la clase y por defecto Economico)
        precio (decimales, ,maximo 5 digitos, 2 decimales)
        posicion (varchar , maximo caracteres 1, choices para elegir la posicion)
        sistema_entretenimiento(hay tv o no)

        Relacion
            vuelo (Muchos a Uno)
            pasajero(Uno a Uno)

Servicio
    Atributos
        tipo de servicio (varchar , maximo 100 caracter)
        costo (decimales)
        duracion del servicio (tiempo)
        añadido del servicio (varchar, maximo 100 caracter)

        Relacion
            aeropuerto (ManyToMany)
        
        Fucnio:
            str (tipo de servicio que se muestra en el admi)

Empleado
    Atributo
        nombre (varchar, maximo 100 caracteres)
        apellido (varchar, maximo 100 caracteres)
        cargo (varchar,maximo 2 caracteres, choices para saber si es jefe o empleado)
        fecha_contratacion (dia y hora)

        Relacion
            Servicio(ManyToMany)
        
        Funcion:
           str: Devuelve nombre apellido y cargo la f es para concadenar  




Ruta
    Atributos:
        clima (varchar de 100)
        destino (varchar de 100)
        comentarios (varchar de 100)
        altura (Entero)

        Relacion:
            origen (muchos a muchos)
            destino (muchos a muchos)
            vuelo (muchos a muchos)

-------------------------------------------------------------------------------------------------------------------
*    Definir en qué consistirá mi página Web

*    Crear repositorio Git de mi página Web

*    Preparar el proyecto Django con nuestra aplicación

*    Definir 10 modelos de mi página Web que cumpla los siguientes requisitos.Al menos 3 relaciones OneToOne, 3 relaciones ManytoOne, 3 relaciones       ManyToMany(Al menos una de ella debe tener una tabla intermedia con atributos extras)

*    Cada modelo debe tener al menos 4 campos.  Y debe exisitr en total 10 atributos de distinto tipo.No son válidos los atributos de relaciones.

*    Debe usasrse al menos 10 parámetros distinto entre todos los atributos creados de todos los modelos.

*    Crear el modelo entidad-relación de la base de datos.

*    En el README.MD debe especificarse en que consiste cada modelo, cada atributo y cada parámetro usado. Y el esquema de modelo entidad-relación.

*    Rellenar las tablas con seeders.

*    Crear un backup de los datos con fixture.

*    No subir a git los archivos que no son necesarios que ya hemos explicado en clase

*    Explicar cualquier código que no se haya visto en clase. Funciones, parámetros, etc..

    Debe entregarse el enlace de git.

-------------------------------------------------------------------------------------------------------------------
ManyToOne = Vuelo(origen) , Vuelo(destino) , Equipaje(pasajero) , Reserva(pasajero) , Reserva(Vuelo)
ManyToMany = Aerolínea(Aeropuerto) , Vuelo(Aerolinea) , Pasajero(vuelo)
OneToOne = ContactoAeropuerto(Aeropuerto) , EstadisticasVuelo(Vuelo), PerfilPasajero(pasajero)




-------------------------------------------------------------------------------------------------------------------

comandos 

source myvenv/bin/activate
python manage.py migrate
python manage.py makemigrations apaeropuerto
python manage.py migrate apaeropuerto
python manage.py seed apaeropuerto --number=20
python manage.py dumpdata --indent 4 > apaeropuerto/fixtures/datos.json

python manage.py createsuperuser
python manage.py runserver