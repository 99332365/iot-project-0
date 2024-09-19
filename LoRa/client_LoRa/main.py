# import sys
# from machine import Pin
# import network
# import socket
# import time
# import struct
# import binascii
# from network import LoRa

# # Configuration LoRa en mode LoRaWAN
# def configurer_lora():
#     lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
#     dev_eui = binascii.unhexlify('0000000000000000')  # Remplacer par ton DevEUI
#     app_eui = binascii.unhexlify('70B3D57ED0012345')  # Remplacer par ton AppEUI
#     app_key = binascii.unhexlify('00000000000000000000000000000000')  # Remplacer par ton AppKey

#     lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

#     while not lora.has_joined():
#         print('Connexion LoRa en cours...')
#         time.sleep(2)

#     print('Connecté à LoRaWAN')
#     return lora

# # Création d'un socket LoRa
# def configurer_socket_lora(lora):
#     s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#     s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  # Définir le débit de données (DR)
#     return s

# # Liste de 10 valeurs de température pour les tests
# temperatures = [25.0, 23.5, 29.3, 15.1, 12.0, 11.2, 13.1, 26.5, 32.0, 50.3]

# def envoyer_temperature_lora(s, temperature):
#     try:
#         payload = struct.pack('f', temperature)  # Convertir la température en bytes
#         s.setblocking(True)
#         s.send(payload)
#         s.setblocking(False)
#         print('Température envoyée (LoRa): {:.2f} °C'.format(temperature))
#     except Exception as e:
#         print("Erreur lors de l'envoi LoRa:", e)

# def envoyer_donnees(s):
#     index = 0
#     while True:
#         try:
#             # Obtenir la température à envoyer
#             temperature = temperatures[index]

#             # Envoyer les données
#             envoyer_temperature_lora(s, temperature)

#             # Passer à la température suivante
#             index = (index + 1) % len(temperatures)

#             time.sleep(5)  # Attendre 5 secondes avant d'envoyer à nouveau

#         except Exception as e:
#             print('Erreur d\'envoi de données: {}'.format(e))

# # Configurer LoRa et démarrer l'envoi des données
# lora = configurer_lora()
# socket_lora = configurer_socket_lora(lora)
# envoyer_donnees(socket_lora)


##
# import sys
# from machine import Pin
# import network
# import socket
# import time
# import struct
# import binascii
# from network import LoRa

# # Configuration LoRa en mode LoRaWAN
# def configurer_lora():
#     lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    
#     # Remplace les valeurs par les tiennes
#     dev_eui = binascii.unhexlify('0000000000000000')  # Ton DevEUI
#     app_eui = binascii.unhexlify('70B3D57ED0012345')  # Ton AppEUI
#     app_key = binascii.unhexlify('00000000000000000000000000000000')  # Ton AppKey

#     lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

#     # Attente de la connexion LoRaWAN
#     while not lora.has_joined():
#         print('Connexion LoRa en cours...')
#         time.sleep(5)  # Augmenté pour éviter de surcharger la connexion

#     print('Connecté à LoRaWAN')
#     return lora

# # Création d'un socket LoRa
# def configurer_socket_lora(lora):
#     s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#     s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  # Débit de données (DR5)
#     s.setblocking(False)  # Non-bloquant pour éviter les blocages en réception/émission
#     return s

# # Liste de 10 valeurs de température pour les tests
# temperatures = [25.0, 23.5, 29.3, 15.1, 12.0, 11.2, 13.1, 26.5, 32.0, 50.3]

# def envoyer_temperature_lora(s, temperature):
#     try:
#         # Conversion de la température en payload (format flottant)
#         payload = struct.pack('f', temperature)
#         s.setblocking(True)  # Bloquer l'envoi pour garantir la transmission
#         s.send(payload)
#         s.setblocking(False)  # Non-bloquant après l'envoi
#         print('Température envoyée (LoRa): {:.2f} °C'.format(temperature))
#     except Exception as e:
#         print("Erreur lors de l'envoi LoRa:", e)

# def envoyer_donnees(s):
#     index = 0
#     while True:
#         try:
#             # Obtenir la température à envoyer
#             temperature = temperatures[index]

#             # Envoyer la température via LoRa
#             envoyer_temperature_lora(s, temperature)

#             # Passer à la température suivante
#             index = (index + 1) % len(temperatures)

#             time.sleep(5)  # Envoyer toutes les 5 secondes

#         except Exception as e:
#             print('Erreur d\'envoi de données: {}'.format(e))

# # Initialisation du LoRa et démarrage de l'envoi des données
# lora = configurer_lora()
# socket_lora = configurer_socket_lora(lora)
# envoyer_donnees(socket_lora)
##import sys
# from machine import Pin
# import network
# import socket
# import time
# import struct
# import binascii
# from network import LoRa

# # Configuration LoRa en mode LoRaWAN
# def configurer_lora():
#     lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)
    
#     # Remplace les valeurs par les tiennes
#     dev_eui = binascii.unhexlify('0000000000000000')  # Ton DevEUI
#     app_eui = binascii.unhexlify('70B3D57ED0012345')  # Ton AppEUI
#     app_key = binascii.unhexlify('00000000000000000000000000000000')  # Ton AppKey

#     lora.join(activation=LoRa.OTAA, auth=(dev_eui, app_eui, app_key), timeout=0)

#     # Attente de la connexion LoRaWAN
#     while not lora.has_joined():
#         print('Connexion LoRa en cours...')
#         time.sleep(5)  # Augmenté pour éviter de surcharger la connexion

#     print('Connecté à LoRaWAN')
#     return lora

# # Création d'un socket LoRa
# def configurer_socket_lora(lora):
#     s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
#     s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)  # Débit de données (DR5)
#     s.setblocking(False)  # Non-bloquant pour éviter les blocages en réception/émission
#     return s

# # Liste de 10 valeurs de température pour les tests
# temperatures = [25.0, 23.5, 29.3, 15.1, 12.0, 11.2, 13.1, 26.5, 32.0, 50.3]

# def envoyer_temperature_lora(s, temperature):
#     try:
#         # Conversion de la température en payload (format flottant)
#         payload = struct.pack('f', temperature)
#         s.setblocking(True)  # Bloquer l'envoi pour garantir la transmission
#         s.send(payload)
#         s.setblocking(False)  # Non-bloquant après l'envoi
#         print('Température envoyée (LoRa): {:.2f} °C'.format(temperature))
#     except Exception as e:
#         print("Erreur lors de l'envoi LoRa:", e)

# def envoyer_donnees(s):
#     index = 0
#     while True:
#         try:
#             # Obtenir la température à envoyer
#             temperature = temperatures[index]

#             # Envoyer la température via LoRa
#             envoyer_temperature_lora(s, temperature)

#             # Passer à la température suivante
#             index = (index + 1) % len(temperatures)

#             time.sleep(30)  # Envoyer toutes les 30 secondes pour ne pas saturer le réseau

#         except Exception as e:
#             print('Erreur d\'envoi de données: {}'.format(e))

# # Initialisation du LoRa et démarrage de l'envoi des données
# lora = configurer_lora()
# socket_lora = configurer_socket_lora(lora)
# envoyer_donnees(socket_lora)
##############################################################

from network import LoRa
import socket
import struct
import time
import machine  # Utilisé pour simuler la température avec un capteur DHT ou un autre capteur

class LoRaClient:
    def __init__(self, client_id, frequency, sf, bandwidth, coding_rate):
        self.client_id = client_id
        self.lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, frequency=frequency, sf=sf, bandwidth=bandwidth, coding_rate=coding_rate)
        self.sock = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
        self.sock.setblocking(False)

    def start(self):
        print("LoRa Client started")

    def get_temperature(self):
        # Simulation d'une température ; remplacer cette ligne avec la lecture réelle d'un capteur de température (par exemple, DHT11)
        return 25.0 + (machine.rng() % 100) / 10.0  # Simuler une température entre 25.0 et 35.0 °C

    def get_mac(self):
        return self.lora.mac()

    def send(self):
        temperature = self.get_temperature()
        mac_addr = self.get_mac()
        data = struct.pack('>If6s', self.client_id, temperature, mac_addr)
        self.sock.send(data)
        # Correction de l'affichage avec la méthode .format()
        print("Sent: client_id={}, temperature={:.2f} °C, mac_addr={}".format(
            self.client_id, temperature, self.format_mac_addr(mac_addr)))

    def format_mac_addr(self, mac_addr):
        return ":".join("{:02x}".format(x) for x in mac_addr)

# Paramètres de configuration LoRa
CLIENT_ID = 1  # Assurez-vous que chaque client a un ID unique
FREQUENCY = 868000000  # 868 MHz pour l'Europe
SPREADING_FACTOR = 7
BANDWIDTH = LoRa.BW_125KHZ
CODING_RATE = LoRa.CODING_4_5

lora_client = LoRaClient(CLIENT_ID, FREQUENCY, SPREADING_FACTOR, BANDWIDTH, CODING_RATE)
lora_client.start()

while True:
    lora_client.send()
    time.sleep(10)  # Envoie toutes les 10 secondes
