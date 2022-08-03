import time

lat = float(input("Digite a latitude: \n-> "))
lon = float(input("Digite a longitude: \n-> "))
google = f'https://maps.google.com/?q={lat},{lon}'

print()
print("          FINDER           ")
print("Latitude -> {}".format(lat))
print("Longitude -> {}".format(lon))

time.sleep(2)
print("Buscando...")
time.sleep(2)
print(google)