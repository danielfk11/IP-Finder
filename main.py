import requests
import json
from urllib.request import urlopen
import folium 

ip = input('-> Coloque o ip que deseja acessar\n-> ')
file = 'infos.json'
file_save = "buscas.txt"

if ip == '':
    print("-> ERROR\n-> Informe um IP")
    exit()

print("Iniciando busca..{}".format(ip))

try:
    if ip:
        url_get_ip = "http://ip-api.com/json/{}".format(ip)

    r = requests.get(url_get_ip)
    rtext = r.text

    with open(file, "w") as textsave:
        textsave.write(rtext)

    request = urlopen(url_get_ip)
    data = request.read().decode()
    data = eval(data)
    print("IP ENCONTRADO\n-> INFOS")
    for i in data:
       print(f"-> {i} = {data[i]}")

    with open(file) as my_json:
        dados = json.load(my_json)
        find_dados = dados

    lat = find_dados['lat'] 
    lon = find_dados['lon'] 

    print("---------------------------------------------------")
    print("-> GOOGLE MAPS\n-> https://maps.google.com/?q={},{}".format(lat, lon))
    print("---------------------------------------------------")

    with open(file_save, 'a') as buscas_save:
        buscas_save.write("\n{}".format(rtext))

except:
    print("************************")
    print("-> ERROR")
    print("************************")

try:
    mapa = folium.Map([lat, lon],               #VERIFICAR ERRO
    files='Staten Terrain',
    zoom_start=16
    )

    addmap = folium.Marker([lat, lon],
    popup='<i>Ip Finder Location<i>',
    tooltip='Vizualizar').add_to(mapa)

    mapa.save(r'.\mapa.html')
    print('Mapa criado com sucesso!\nMapa -> http://127.0.0.1:5500/mapa.html')
    print("---------------------------------------------------")
except:
    print("error")
