'''
Script hecho por Andrés David Chavarría Palma.
https://mastodon.cr/@tunkuluchu
Creado el 11 de Marzo del 2025.
'''

from PIL import Image, ImageSequence
import requests
import time

#------------ CONFIG ------------------
imagen = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/cam/GEOCOLOR/GOES16-CAM-GEOCOLOR-1000x1000.gif'

api_text = 'https://mastodon.cr/api/v1/statuses'
api_imagen = 'https://mastodon.cr/api/v2/media'

encabezados = {
    'Authorization': 'Bearer ' + 'TOKEN_AQUÍ'
}

#------------ TRATAMIENTO IMAGEN ------
#Descarga
print('Descargando imagen.')
with open('imagen.gif', 'wb') as f:
    f.write(requests.get(imagen).content)
print('Imagen descargada.')

#Redimensionar imagen
print('Redimensionando imagen.')
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
print('Imagen redimensionada.')

#------------ API MASTODON --------
#Fase Imagen
print('Publicando media.')
imagen = {
    'file': ('goes_tiempoac',open("animacion.gif", "rb"),'image/gif'),
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
        'media_ids[]': [id_imagen],
        'visibility': 'direct'
    }
    
    req = requests.request('POST',api_text,data=toot,headers=encabezados)
    print(req)
    print('Publicado.')

elif req.status_code == 202:
    id_imagen = req.json()['id']
    sitio = 'https://mastodon.cr/api/v1/media/' + id_imagen

    while req.status_code in (202,206):
        print(req)
        time.sleep(60)
        req = requests.request('GET',sitio,headers=encabezados)
    
    if req.status_code == 200:
        toot = {
        'status': '-Publicación automática-\n\nCondiciones atmosféricas actuales en #AméricaCentral.\n\nFuente: National Oceanic and Atmospheric Administration.\n\n#GOES16 #NOAA',
        'media_ids[]': [id_imagen],
        'visibility': 'direct'
        }
        
        req = requests.request('POST',api_text,data=toot,headers=encabezados)
        print(req)
        print('Publicado.')
    
    else:
        print('Problema en el procesamiento.')
        print(req.json())

else:
    print('Problema en la subida.')
    print(req.json())