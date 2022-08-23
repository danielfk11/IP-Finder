Linguagem utilizada

    python 3.6

Imports

    import requests
    import json
    from urllib.request import urlopen  
    import folium

Formato 

    IP 

Como funciona?

Digite um IP no qual voce deseja buscar como por exemplo o 8.8.8.8 DNS do google.

Como o sistema funciona?

Utilizando a funcionalidade das bibliotecas ele pega atraves de uma api as informacos do IP e salva em um .json, assim podendo pegar as informacoes da latitude e longitude para fazer uma busca no Google Maps. Salvando todas as buscas em um buscas.txt.

