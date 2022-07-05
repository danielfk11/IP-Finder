import requests
import json
from urllib.request import urlopen

ip = input('-> Coloque o ip que deseja acessar\n-> ')
print("Iniciando busca..{}".format(ip))
file = 'infos.json'

try:
    if ip:
        url_get_ip = "http://ip-api.com/json/{}".format(ip)

    r = requests.get(url_get_ip)
    rtext = r.text

    with open("infos.json", "w") as textsave:
        textsave.write(rtext)

    request = urlopen(url_get_ip)
    data = request.read().decode()
    data = eval(data)
    print("IP ENCONTRADO\n-> INFOS")
    for i in data:
       print(f"-> {i} = {data[i]}")

    with open("infos.json") as my_json:
        dados = json.load(my_json)
        find_dados = dados

    lat =  find_dados['lat'] 
    lon = find_dados['lon'] 

    print("---------------------------------------------------")
    print("-> GOOGLE MAPS\n-> https://maps.google.com/?q={},{}".format(lat, lon))
    print("---------------------------------------------------")

    with open("buscas.txt", 'a') as buscas_save:
        buscas_save.write("\n{}".format(rtext))

except:
    print("************************")
    print("error")
    print("************************")