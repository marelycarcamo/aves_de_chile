# Generador de HTML para Aves de Chile

## Descripción 
Genrador de HTML Galería de Aves de Chile. Este programa en Python descarga datos de aves desde la API 'https://aves.ninjas.cl/api/birds', genera un archivo HTML con la información de las aves y lo guarda en el archivo 'index.html'.

## Tecnologías Aplicadas

- **Python**: El programa está escrito en Python, un lenguaje de programación de alto nivel que es fácil de aprender y potente, lo que lo hace ideal para el desarrollo rápido de aplicaciones.

- **Requests**: Se utiliza la biblioteca `requests` de Python para hacer solicitudes HTTP a la API.

- **JSON**: Se utiliza JSON para estructurar los datos que se obtienen de la API.

- **HTML y CSS**: Se genera un archivo HTML con CSS para presentar la información de las aves de una manera fácil de leer.

## Calidad del Código

El código está bien organizado y sigue las mejores prácticas de Python. Las funciones están claramente definidas y cada una realiza una tarea específica, lo que facilita la comprensión del código. Además, se utilizan comentarios para explicar qué hace cada parte del código, lo que hace que el código sea más legible y fácil de mantener.

## Utilidad para el Aprendizaje de Nuevos Desarrolladores

Este programa es un excelente recurso para los nuevos desarrolladores que están aprendiendo a trabajar con APIs, JSON y la generación de archivos HTML en Python. Proporciona un ejemplo práctico de cómo se pueden utilizar estas tecnologías para descargar datos de una API, procesar esos datos y generar un archivo HTML a partir de ellos.

Además, el código está escrito de una manera que es fácil de entender, lo que hace que sea un excelente recurso para aprender buenas prácticas de codificación en Python.

## Funciones

El programa consta de las siguientes funciones:

- `obtener_datos_aves(url)`: Esta función descarga datos de aves desde la API proporcionada y los decodifica en JSON.

- `generar_html_aves(datos_aves)`: Esta función genera el HTML con la información de las aves. Crea una tarjeta para cada ave con su imagen, nombre en español y nombre en inglés.

- `main()`: Esta es la función principal del programa. Obtiene los datos de las aves, genera el HTML y lo guarda en el archivo 'index.html'.

## Uso

Para usar este programa, simplemente ejecuta el archivo Python en tu entorno de Python. Asegúrate de tener instalado el módulo 'requests' de Python.

```bash
python nombre_del_archivo.py
```
Después de ejecutar el programa, deberías ver el mensaje “¡Archivo HTML creado exitosamente!” y deberías encontrar el archivo ‘index.html’ en el mismo directorio que el archivo Python.

## Dependencias
Este programa depende del módulo ‘requests’ de Python. Puedes instalarlo con pip:

```bash
pip install requests
```

Por favor, reemplaza "nombre_del_archivo.py" con el nombre real de tu archivo Python. Espero que esto te sea útil. 😊
