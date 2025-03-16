import logging
from PIL import Image, ImageSequence
import requests
import time

#------------ CONFIG ------------------
logging.basicConfig(filename='log_app2.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
imagen = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/cam/GEOCOLOR/GOES16-CAM-GEOCOLOR-1000x1000.gif'
api_text = 'https://bots.fedi.cr/api/v1/statuses'
api_imagen = 'https://bots.fedi.cr/api/v2/media'
encabezados = {
    'Authorization': 'Bearer ' + 'TOKEN_AQUÍ'
}

#------------ TRATAMIENTO IMAGEN ------
#Descarga
logging.info('Descargando imagen.')
with open('imagen.gif', 'wb') as f:
    f.write(requests.get(imagen).content)
logging.info('Imagen descargada.')

#Redimensionar imagen
logging.info('Redimensionando imagen.')
size = 500, 500
im = Image.open("imagen.gif")
frames = ImageSequence.Iterator(im)

def thumbnails(frames):
    for frame in frames:
        thumbnail = frame.copy()
        thumbnail.thumbnail(size, Image.LANCZOS)
        yield thumbnail

frames = thumbnails(frames)
om = next(frames)
om.info = im.info
om.save("animacion.gif", save_all=True, append_images=list(frames))
logging.info('Imagen redimensionada.')

#------------ API MASTODON --------
#Fase Imagen
logging.info('Publicando media.')
imagen = {
    'file': ('goes_tiempoac',open("animacion.gif", "rb"),'image/gif'),
}
imagen_params= {
    'description': 'Animación de imágenes satelitales que ilustran las condiciones atmosféricas sobre el territorio de América Central.'
}

req = requests.request('POST',api_imagen,headers=encabezados,files=imagen, data=imagen_params)

#Fase Toot

if req.status_code == 200:
    id_imagen = req.json()['id']
    toot = {
        'status': '-* Publicación automática *-\n\nCondiciones atmosféricas en las últimas 8 horas en #AméricaCentral.\n\nFuente: National Oceanic and Atmospheric Administration.\n\n#GOES #NOAA',
        'media_ids[]': [id_imagen]
    }
    
    req = requests.request('POST',api_text,data=toot,headers=encabezados)
    logging.info(req)
    logging.info('Publicado.')

elif req.status_code == 202:
    id_imagen = req.json()['id']
    sitio = 'https://bots.fedi.cr/api/v1/media/' + id_imagen

    while req.status_code in (202,206):
        logging.info(req)
        time.sleep(60)
        req = requests.request('GET',sitio,headers=encabezados)
    
    if req.status_code == 200:
        toot = {
        'status': '-* Publicación automática *-\n\nCondiciones atmosféricas en las últimas 8 horas en #AméricaCentral.\n\nFuente: National Oceanic and Atmospheric Administration.\n\n#GOES16 #NOAA',
        'media_ids[]': [id_imagen]
        }
        
        req = requests.request('POST',api_text,data=toot,headers=encabezados)
        logging.info(req)
        logging.info('Publicado.')
    
    else:
        logging.info('Problema en el procesamiento.')
        logging.info(req.json())

else:
    logging.info('Problema en la subida.')
    logging.info(req.json())