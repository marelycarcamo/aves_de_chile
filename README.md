# Generador de HTML para Aves de Chile

Este programa en Python descarga datos de aves desde la API 'https://aves.ninjas.cl/api/birds', genera un archivo HTML con la información de las aves y lo guarda en el archivo 'index.html'.

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
