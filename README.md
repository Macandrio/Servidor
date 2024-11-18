comandos 

python3 -m venv myvenv
source myvenv/bin/activate

python -m pip install --upgrade pip
pip install -r requirements.txt

python manage.py migrate
python manage.py makemigrations apaeropuerto
python manage.py migrate apaeropuerto
python manage.py seed apaeropuerto --number=20
python manage.py dumpdata --indent 4 > apaeropuerto/fixtures/datos.json
python manage.py loaddata apaeropuerto/fixtures/datos.json

python manage.py createsuperuser
python manage.py runserver

1. date
Formatea una fecha.
Ejemplo: {{ fecha|date:"D M Y" }}
2. length
Retorna la longitud de una cadena o el número de elementos en una lista.
Ejemplo: {{ lista|length }}
3. default
Proporciona un valor predeterminado si la variable está vacía.
Ejemplo: {{ variable|default:"Sin valor" }}
4. lower
Convierte una cadena a minúsculas.
Ejemplo: {{ texto|lower }}
5. upper
Convierte una cadena a mayúsculas.
Ejemplo: {{ texto|upper }}
6. yesno
Convierte valores booleanos a texto personalizado.
Ejemplo: {{ valor_booleano|yesno:"Sí,No,Quizás" }}
7. truncatechars
Trunca una cadena después de un número de caracteres.
Ejemplo: {{ texto_largo|truncatechars:20 }}
8. default_if_none
Proporciona un valor predeterminado si la variable es None.
Ejemplo: {{ variable|default_if_none:"Valor predeterminado" }}
9. slice
Extrae una parte de una lista o cadena.
Ejemplo: {{ lista|slice:":3" }}
10. pluralize
Añade un sufijo plural cuando sea necesario.
Ejemplo: {{ contador }} comentario{{ contador|pluralize }}
11. join
Une una lista con un carácter o una cadena.
Ejemplo: {{ lista|join:", " }}
12. escape
Escapa caracteres HTML.
Ejemplo: {{ texto|escape }}
13. add
Suma un valor a una variable.
Ejemplo: {{ numero|add:"10" }}
14. divisibleby
Verifica si un número es divisible por otro.
Ejemplo: {% if numero|divisibleby:3 %}Es divisible{% endif %}
15. striptags
Elimina etiquetas HTML de una cadena.
Ejemplo: {{ texto|striptags }}
16. filesizeformat
Formatea el tamaño de un archivo de manera legible.
Ejemplo: {{ archivo.size|filesizeformat }}
17. capfirst
Capitaliza la primera letra de una cadena.
Ejemplo: {{ texto|capfirst }}
18. wordcount
Cuenta el número de palabras en una cadena.
Ejemplo: {{ texto|wordcount }}
19. linebreaks
Convierte líneas nuevas en etiquetas <p> y <br>.
Ejemplo: {{ texto|linebreaks }}
20. title
Convierte una cadena en "Title Case" (Primera letra de cada palabra en mayúscula).
Ejemplo: {{ texto|title }}
21. dictsort
Ordena una lista de diccionarios por la clave dada.
Ejemplo: {{ lista_diccionarios|dictsort:"clave" }}
22. removetags
Elimina etiquetas HTML específicas de una cadena.
Ejemplo: {{ texto|removetags:"b" }}
23. floatformat
Formatea un número de punto flotante.
Ejemplo: {{ numero|floatformat:2 }}
24. cut
Elimina todas las ocurrencias de una cadena dada.
Ejemplo: {{ texto|cut:"caracter" }}
25. wordwrap
Envuelve una cadena a un ancho específico.
Ejemplo: {{ texto|wordwrap:20 }}
26. make_list
Convierte una cadena en una lista de caracteres.
Ejemplo: {{ texto|make_list }}