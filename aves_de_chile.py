import requests


def obtener_datos_aves(url):
    # Descarga datos de aves desde la API y los decodifica en JSON
    respuesta = requests.get(url)
    return respuesta.json()


def generar_html_aves(datos_aves):
    # Genera el HTML con la información de las aves
    contenido_cuerpo = ""
    from string import Template


    for ave in datos_aves:
        url_imagen = ave['images']['main']
        nombre_espanol = ave['name']['spanish']
        nombre_ingles = ave['name']['english']

    # Creación de la card para cada ave
        informacion_ave = f"""
<div class='card'>
	<img src="{url_imagen}" alt="{nombre_espanol}">
	<div>
    	<h2 class="card-title">{nombre_espanol}</h2>
    	<h4 class="card-text">{nombre_ingles}</h4>
  	</div>
</div>
"""

        contenido_cuerpo += informacion_ave

    plantilla_html = Template("""<!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="css/style.css">
    <title>Aves de Chile</title>
    </head>
    <body>

    <h1>Aves de Chile</h1>
    <div id='container-cards'>
    $contenido_cuerpo
    </div>
    </body>
    </html>
    """)

    html_final = plantilla_html.substitute(contenido_cuerpo=contenido_cuerpo)
    return html_final


def main():
    url_datos_aves = 'https://aves.ninjas.cl/api/birds'
    datos_aves = obtener_datos_aves(url_datos_aves)

    html_aves = generar_html_aves(datos_aves)

    with open('aves_de_chile.html', 'w') as f:
        f.write(html_aves)

    print("¡Archivo HTML creado exitosamente!")


if __name__ == '__main__':
    main()

