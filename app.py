'''
Script hecho por Andrés David Chavarría Palma.
https://mastodon.cr/@tunkuluchu
Creado el 10 de Marzo del 2025.
'''
import logging
import requests
import time

#------------ CONFIG ------------------
logging.basicConfig(filename='log_app.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
imagen = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/cam/GEOCOLOR/2000x2000.jpg'
api_text = 'https://mastodon.cr/api/v1/statuses'
api_imagen = 'https://mastodon.cr/api/v2/media'
encabezados = {
    'Authorization': 'Bearer ' + 'TOKEN_AQUÍ'
}

#------------ TRATAMIENTO IMAGEN ------
#Descarga
logging.info('/ INICIO / Descargando imagen.')
with open('imagen.jpg', 'wb') as f:
    f.write(requests.get(imagen).content)
logging.info('Imagen descargada.')

#------------ API MASTODON --------
#Fase Imagen
logging.info('Publicando media.')
imagen = {
    'file': ('goes_tiempoac',open("imagen.jpg", "rb"),'image/jpg'),
}
imagen_params= {
    'description': 'Animación de imágenes satelitales que ilustran las condiciones atmosféricas y el porcentaje de nubosidad sobre el territorio de América Central.'
}

req = requests.request('POST',api_imagen,headers=encabezados,files=imagen, data=imagen_params)

#Fase Toot

if req.status_code == 200:
    id_imagen = req.json()['id']
    toot = {
        'status': '-Publicación automática-\n\nCondiciones atmosféricas actuales en #AméricaCentral.\n\nFuente: National Oceanic and Atmospheric Administration.\n\n#GOES #NOAA',
        'media_ids[]': [id_imagen]
    }
    
    req = requests.request('POST',api_text,data=toot,headers=encabezados)
    logging.info(req)
    logging.info('/ FIN / Publicado.')

elif req.status_code == 202:
    id_imagen = req.json()['id']
    sitio = 'https://mastodon.cr/api/v1/media/' + id_imagen

    while req.status_code in (202,206):
        logging.info(req)
        time.sleep(60)
        req = requests.request('GET',sitio,headers=encabezados)
    
    if req.status_code == 200:
        toot = {
        'status': '-Publicación automática-\n\nCondiciones atmosféricas actuales en #AméricaCentral.\n\nFuente: National Oceanic and Atmospheric Administration.\n\n#GOES16 #NOAA',
        'media_ids[]': [id_imagen]
        }
        
        req = requests.request('POST',api_text,data=toot,headers=encabezados)
        logging.info(req)
        logging.info('/ FIN / Publicado.')
    
    else:
        logging.info('/ FIN / Problema en el procesamiento.')
        logging.info(req.json())

else:
    logging.info('/ FIN / Problema en la subida.')
    logging.info(req.json())