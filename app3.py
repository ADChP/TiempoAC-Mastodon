'''
Tiempo América Central - App # 3
Script hecho por ADChP
@tunkuluchu@mastodon.cr
Alajuela, Costa Rica.
Abril, 2025
'''

import logging
import requests

#------------ CONFIG ------------------
logging.basicConfig(filename='log_app3.log', encoding='utf-8', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
consulta = 'https://api.open-meteo.com/v1/forecast?latitude=17.25251637031138,14.630743672173088,13.693826768607298,14.059342797874544,12.117116601690624,9.927934126520256,8.982205382794353&longitude=-88.76667079027592,-90.49871661797538,-89.21229620340385,-87.18405520940287,-86.23477633806557,-84.08622381241818,-79.51552268487558&current=temperature_2m,precipitation,weather_code,relative_humidity_2m,wind_speed_10m,wind_direction_10m,cloud_cover&timezone=auto'
api_text = 'https://bots.fedi.cr/api/v1/statuses'
encabezados = {
    'Authorization': 'Bearer ' + 'TOKEN_AQUÍ'
}
capitales = ['Belmopán','Ciudad de Guatemala','San Salvador','Tegucigalpa',
                  'Managua','San José','Ciudad de Panamá']

#Códigos de observación según la Organización Meteorológica Mundial.
wmo_cods = {0:'Cielo despejado.',
                1:'Principalmente despejado.',
                2:'Parcialmente nublado.',
                3:'Nublado.',
                45:'Niebla.',
                48:'Niebla de escarcha.',
                51:'Llovizna de intensidad ligera.',
                53:'Llovizna de intensidad moderada.',
                55:'Llovizna de intensidad densa.',
                56:'Llovizna helada de intensidad ligera.',
                57:'Llovizna helada de intensidad densa.',
                61:'Lluvia de intensidad ligera.',
                63:'Lluvia de intensidad moderada.',
                65:'Lluvia de intensidad fuerte.',
                66:'Lluvia helada de intensidad ligera.',
                67:'Lluvia helada de intensidad fuerte.',
                71:'Caída de nieve de intensidad ligera.',
                73:'Caída de nieve de intensidad moderada.',
                75:'Caída de nieve de intensidad fuerte.',
                77:'Granos de nieve.',
                80:'Chubascos de intensidad ligera.',
                81:'Chubascos de intensidad moderada.',
                82:'Chubascos de intensidad violenta.',
                85:'Chubascos de nieve ligera.',
                86:'Chubascos de nieve fuerte.',
                95:'Tormenta.',
                96:'Tormenta con ligero granizo.',
                99:'Tormenta con fuerte granizo.'}

#------------ PUBLICACIÓN ------------------
#Obtención de datos.
logging.info('/ INICIO / Descargando datos de Open-Meteo.')
req = requests.request('GET',consulta)

if req.status_code == 200:
    logging.info('Almacenando datos.')
    req = req.json()
    datos = [{'capital': capitales[y],
            'temp': x['current']['temperature_2m'],
            'precip': x['current']['precipitation'],
            'codigo': x['current']['weather_code'],
            'hum_rel': x['current']['relative_humidity_2m'],
            'vel_viento': x['current']['wind_speed_10m'],
            'dir_viento': x['current']['wind_direction_10m'],
            'cob_nub': x['current']['cloud_cover'],
            'fecha_hora': x['current']['time']} for x,y in zip(req,range(0,7))]

    texto = f'''Condiciones actuales del tiempo en las capitales de #AméricaCentral.

(T: Temperatura, P: Precipitación, HR: Humedad relativa, VV: Velocidad del viento, DV: Dirección del viento, Nub: Cobertura de nubosidad)

{datos[0]['capital']} 🇧🇿:
T: {datos[0]['temp']}°C
P: {datos[0]['precip']} mm
HR: {datos[0]['hum_rel']}%
VV: {datos[0]['vel_viento']} km/h
DV: {'N' if datos[0]['dir_viento'] in range(0,11) or datos[0]['dir_viento'] in range(350,361) else 'NNE' if datos[0]['dir_viento'] in range(11,40) else 'NE' if datos[0]['dir_viento'] in range(40,51) else 'ENE' if datos[0]['dir_viento'] in range(51,80) else 'E' if datos[0]['dir_viento'] in range(80,101) else 'ESE' if datos[0]['dir_viento'] in range(101,121) else 'SE' if datos[0]['dir_viento'] in range(121,141) else 'SSE' if datos[0]['dir_viento'] in range(141,170) else 'S' if datos[0]['dir_viento'] in range(170,191) else 'SSO' if datos[0]['dir_viento'] in range(191,211) else 'SO' if datos[0]['dir_viento'] in range(211,231) else 'OSO' if datos[0]['dir_viento'] in range(231,260) else 'O' if datos[0]['dir_viento'] in range(260,281) else 'ONO' if datos[0]['dir_viento'] in range(281,301) else 'NO' if datos[0]['dir_viento'] in range(301,321) else 'NNO' if datos[0]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[0]['cob_nub']}%
{wmo_cods[datos[0]['codigo']]}

{datos[1]['capital']} 🇬🇹:
T: {datos[1]['temp']}°C
P: {datos[1]['precip']} mm
HR: {datos[1]['hum_rel']}%
VV: {datos[1]['vel_viento']} km/h
DV: {'N' if datos[1]['dir_viento'] in range(0,11) or datos[1]['dir_viento'] in range(350,361) else 'NNE' if datos[1]['dir_viento'] in range(11,40) else 'NE' if datos[1]['dir_viento'] in range(40,51) else 'ENE' if datos[1]['dir_viento'] in range(51,80) else 'E' if datos[1]['dir_viento'] in range(80,101) else 'ESE' if datos[1]['dir_viento'] in range(101,121) else 'SE' if datos[1]['dir_viento'] in range(121,141) else 'SSE' if datos[1]['dir_viento'] in range(141,170) else 'S' if datos[1]['dir_viento'] in range(170,191) else 'SSO' if datos[1]['dir_viento'] in range(191,211) else 'SO' if datos[1]['dir_viento'] in range(211,231) else 'OSO' if datos[1]['dir_viento'] in range(231,260) else 'O' if datos[1]['dir_viento'] in range(260,281) else 'ONO' if datos[1]['dir_viento'] in range(281,301) else 'NO' if datos[1]['dir_viento'] in range(301,321) else 'NNO' if datos[1]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[1]['cob_nub']}%
{wmo_cods[datos[1]['codigo']]}

{datos[2]['capital']} 🇸🇻:
T: {datos[2]['temp']}°C
P: {datos[2]['precip']} mm
HR: {datos[2]['hum_rel']}%
VV: {datos[2]['vel_viento']} km/h
DV: {'N' if datos[2]['dir_viento'] in range(0,11) or datos[2]['dir_viento'] in range(350,361) else 'NNE' if datos[2]['dir_viento'] in range(11,40) else 'NE' if datos[2]['dir_viento'] in range(40,51) else 'ENE' if datos[2]['dir_viento'] in range(51,80) else 'E' if datos[2]['dir_viento'] in range(80,101) else 'ESE' if datos[2]['dir_viento'] in range(101,121) else 'SE' if datos[2]['dir_viento'] in range(121,141) else 'SSE' if datos[2]['dir_viento'] in range(141,170) else 'S' if datos[2]['dir_viento'] in range(170,191) else 'SSO' if datos[2]['dir_viento'] in range(191,211) else 'SO' if datos[2]['dir_viento'] in range(211,231) else 'OSO' if datos[2]['dir_viento'] in range(231,260) else 'O' if datos[2]['dir_viento'] in range(260,281) else 'ONO' if datos[2]['dir_viento'] in range(281,301) else 'NO' if datos[2]['dir_viento'] in range(301,321) else 'NNO' if datos[2]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[2]['cob_nub']}%
{wmo_cods[datos[2]['codigo']]}

{datos[3]['capital']} 🇭🇳:
T: {datos[3]['temp']}°C
P: {datos[3]['precip']} mm
HR: {datos[3]['hum_rel']}%
VV: {datos[3]['vel_viento']} km/h
DV: {'N' if datos[3]['dir_viento'] in range(0,11) or datos[3]['dir_viento'] in range(350,361) else 'NNE' if datos[3]['dir_viento'] in range(11,40) else 'NE' if datos[3]['dir_viento'] in range(40,51) else 'ENE' if datos[3]['dir_viento'] in range(51,80) else 'E' if datos[3]['dir_viento'] in range(80,101) else 'ESE' if datos[3]['dir_viento'] in range(101,121) else 'SE' if datos[3]['dir_viento'] in range(121,141) else 'SSE' if datos[3]['dir_viento'] in range(141,170) else 'S' if datos[3]['dir_viento'] in range(170,191) else 'SSO' if datos[3]['dir_viento'] in range(191,211) else 'SO' if datos[3]['dir_viento'] in range(211,231) else 'OSO' if datos[3]['dir_viento'] in range(231,260) else 'O' if datos[3]['dir_viento'] in range(260,281) else 'ONO' if datos[3]['dir_viento'] in range(281,301) else 'NO' if datos[3]['dir_viento'] in range(301,321) else 'NNO' if datos[3]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[3]['cob_nub']}%
{wmo_cods[datos[3]['codigo']]}

{datos[4]['capital']} 🇳🇮:
T: {datos[4]['temp']}°C
P: {datos[4]['precip']} mm
HR: {datos[4]['hum_rel']}%
VV: {datos[4]['vel_viento']} km/h
DV: {'N' if datos[4]['dir_viento'] in range(0,11) or datos[4]['dir_viento'] in range(350,361) else 'NNE' if datos[4]['dir_viento'] in range(11,40) else 'NE' if datos[4]['dir_viento'] in range(40,51) else 'ENE' if datos[4]['dir_viento'] in range(51,80) else 'E' if datos[4]['dir_viento'] in range(80,101) else 'ESE' if datos[4]['dir_viento'] in range(101,121) else 'SE' if datos[4]['dir_viento'] in range(121,141) else 'SSE' if datos[4]['dir_viento'] in range(141,170) else 'S' if datos[4]['dir_viento'] in range(170,191) else 'SSO' if datos[4]['dir_viento'] in range(191,211) else 'SO' if datos[4]['dir_viento'] in range(211,231) else 'OSO' if datos[4]['dir_viento'] in range(231,260) else 'O' if datos[4]['dir_viento'] in range(260,281) else 'ONO' if datos[4]['dir_viento'] in range(281,301) else 'NO' if datos[4]['dir_viento'] in range(301,321) else 'NNO' if datos[4]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[4]['cob_nub']}%
{wmo_cods[datos[4]['codigo']]}

{datos[5]['capital']} 🇨🇷:
T: {datos[5]['temp']}°C
P: {datos[5]['precip']} mm
HR: {datos[5]['hum_rel']}%
VV: {datos[5]['vel_viento']} km/h
DV: {'N' if datos[5]['dir_viento'] in range(0,11) or datos[5]['dir_viento'] in range(350,361) else 'NNE' if datos[5]['dir_viento'] in range(11,40) else 'NE' if datos[5]['dir_viento'] in range(40,51) else 'ENE' if datos[5]['dir_viento'] in range(51,80) else 'E' if datos[5]['dir_viento'] in range(80,101) else 'ESE' if datos[5]['dir_viento'] in range(101,121) else 'SE' if datos[5]['dir_viento'] in range(121,141) else 'SSE' if datos[5]['dir_viento'] in range(141,170) else 'S' if datos[5]['dir_viento'] in range(170,191) else 'SSO' if datos[5]['dir_viento'] in range(191,211) else 'SO' if datos[5]['dir_viento'] in range(211,231) else 'OSO' if datos[5]['dir_viento'] in range(231,260) else 'O' if datos[5]['dir_viento'] in range(260,281) else 'ONO' if datos[5]['dir_viento'] in range(281,301) else 'NO' if datos[5]['dir_viento'] in range(301,321) else 'NNO' if datos[5]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[5]['cob_nub']}%
{wmo_cods[datos[5]['codigo']]}

{datos[6]['capital']} 🇵🇦:
T: {datos[6]['temp']}°C
P: {datos[6]['precip']} mm
HR: {datos[6]['hum_rel']}%
VV: {datos[6]['vel_viento']} km/h
DV: {'N' if datos[6]['dir_viento'] in range(0,11) or datos[6]['dir_viento'] in range(350,361) else 'NNE' if datos[6]['dir_viento'] in range(11,40) else 'NE' if datos[6]['dir_viento'] in range(40,51) else 'ENE' if datos[6]['dir_viento'] in range(51,80) else 'E' if datos[6]['dir_viento'] in range(80,101) else 'ESE' if datos[6]['dir_viento'] in range(101,121) else 'SE' if datos[6]['dir_viento'] in range(121,141) else 'SSE' if datos[6]['dir_viento'] in range(141,170) else 'S' if datos[6]['dir_viento'] in range(170,191) else 'SSO' if datos[6]['dir_viento'] in range(191,211) else 'SO' if datos[6]['dir_viento'] in range(211,231) else 'OSO' if datos[6]['dir_viento'] in range(231,260) else 'O' if datos[6]['dir_viento'] in range(260,281) else 'ONO' if datos[6]['dir_viento'] in range(281,301) else 'NO' if datos[6]['dir_viento'] in range(301,321) else 'NNO' if datos[6]['dir_viento'] in range(321,350) else 'No disponible'}
Nub: {datos[6]['cob_nub']}%
{wmo_cods[datos[6]['codigo']]}

Fuente: Open-Meteo.
'''
    #Publicación de toot.
    logging.info('Publicando toot.')
    toot = {'status':texto,
            'visibility': 'direct'}
    mastodon = requests.request('POST',api_text,data=toot,headers=encabezados)

else:
    logging.info('/ FIN / Petición fallida.')