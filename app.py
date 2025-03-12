'''
Script hecho por Andrés David Chavarría Palma.
https://mastodon.cr/@tunkuluchu
Creado el 10 de Marzo del 2025.
'''
import requests

#------------ CONFIG
imagen = 'https://cdn.star.nesdis.noaa.gov/GOES16/ABI/SECTOR/cam/GEOCOLOR/2000x2000.jpg'

api_text = 'https://mastodon.cr/api/v1/statuses'
api_imagen = 'https://mastodon.cr/api/v2/media'

encabezados = {
    'Authorization': 'Bearer ' + 'TOKEN_AQUÍ'
}

#------------ REQUEST IMAGEN
with open('imagen.jpg', 'wb') as f:
    f.write(requests.get(imagen).content)

#------------ API MASTODON
#Fase Imagen

imagen = {
    'file': ('goes_tiempoac',open("imagen.jpg", "rb"),'image/jpg'),
}
imagen_params= {
    'description': 'Imagen satelital que ilustra las condiciones atmosféricas y el porcentaje de nubosidad sobre el territorio de América Central.'
}

req = requests.request('POST',api_imagen,headers=encabezados,files=imagen, data=imagen_params)
id_imagen = req.json()['id']

#Fase Toot
toot = {
    'status': '-Publicación automática-\n\nCondiciones atmosféricas actuales en #AméricaCentral.\n\nFuente: National Oceanic and Atmospheric Administration.\n\n#GOES16 #NOAA',
    'media_ids[]': [id_imagen]
}

req = requests.request('POST',api_text,data=toot,headers=encabezados)