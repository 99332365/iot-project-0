from network import Bluetooth, WLAN, LoRa
import struct
import socket
import time
import _thread as thread

# Configuration du réseau Wi-Fi
SSID = 'IoT IMT Nord Europe'
PASSWORD = '72Hin@R*'

# Variable globale pour stocker l'adresse IP Wi-Fi
wlan_ip = None

def configurer_reseau():
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(SSID, auth=(WLAN.WPA2, PASSWORD))

    while not wlan.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)

    global wlan_ip
    wlan_ip = wlan.ifconfig()[0]
    print('Connected to Wi-Fi, IP Address: {}'.format(wlan_ip))
    return wlan_ip

def envoyer_temperature_tcp_sender(temperature):
    command = 'Temperature: {}\n'.format(temperature)
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.connect(('10.89.1.86', 1235))  # Adresse IP du TcpSenderNode
            conn.send(command.encode())
            print('Température envoyée: {}'.format(command.strip()))
    except Exception as e:
        print('Erreur d\'envoi de température: {}'.format(e))

# Initialisation du Bluetooth
bluetooth = Bluetooth()
bluetooth.init()
SERVICE_UUID = 0xec00
CHARACTERISTIC_UUID = 0xec0e

def handle_client(value):
    """Gère les données reçues d'un client BLE."""
    try:
        temperature = struct.unpack('f', value)[0]
        print("Température reçue (BLE): {:.2f} °C".format(temperature))
        envoyer_temperature_tcp_sender(temperature)
    except Exception as e:
        print("Erreur lors du traitement des données reçues:", e)

def conn_cb(event):
    """Callback pour les événements de connexion/déconnexion."""
    if event == Bluetooth.CLIENT_CONNECTED:
        print('Client connecté')
    elif event == Bluetooth.CLIENT_DISCONNECTED:
        print('Client déconnecté')

def chr1_handler(chr, value):
    """Callback pour gérer les données reçues dans la caractéristique."""
    try:
        value = value[1] if isinstance(value, tuple) and len(value) > 1 else value
        handle_client(value)
    except Exception as e:
        print("Erreur dans le handler de caractéristique:", e)

# Serveur TCP
def serveur_tcp():
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((wlan_ip, port))
        s.listen(1)
        print('Serveur TCP en écoute sur {}:{}'.format(wlan_ip, port))

        while True:
            conn, _ = s.accept()
            print('Connexion acceptée')
            with conn:
                while True:
                    data = conn.recv(1024).decode()
                    if not data:
                        break
                    print('Données reçues (Wi-Fi): {}'.format(data.strip()))
                    if data.startswith('Temperature:'):
                        temperature = data.split(':')[1].strip()
                        print('Température reçue (Wi-Fi): {}'.format(temperature))
                        envoyer_temperature_tcp_sender(temperature)
                    conn.send('Message reçu et traité\n'.encode())

# Serveur BLE
def serveur_ble():
    bluetooth.set_advertisement(name='FiPy Server', service_uuid=SERVICE_UUID)
    bluetooth.advertise(True)
    srv1 = bluetooth.service(uuid=SERVICE_UUID, isprimary=True, nbr_chars=1)
    chr1 = srv1.characteristic(uuid=CHARACTERISTIC_UUID, value=b'')
    chr1.callback(trigger=Bluetooth.CHAR_WRITE_EVENT, handler=chr1_handler)
    bluetooth.callback(trigger=Bluetooth.CLIENT_CONNECTED | Bluetooth.CLIENT_DISCONNECTED, handler=conn_cb)

    print('Serveur BLE démarré et en attente de connexions...')
    while True:
        time.sleep(1)

# Serveur LoRa
def serveur_lora():
    lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868, frequency=868000000, sf=7)
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    s.setblocking(False)

    print('Serveur LoRa démarré et en attente de données...')
    while True:
        data = s.recv(256)
        if data:
            client_id, temperature = struct.unpack('>If', data[:8])
            print('Température reçue (LoRa) de client {}: {:.2f} °C'.format(client_id, temperature))
            envoyer_temperature_tcp_sender(temperature)
        time.sleep(1)

# Démarrage du réseau Wi-Fi
wlan_ip = configurer_reseau()

# Démarrage des serveurs dans des threads séparés
thread.start_new_thread(serveur_tcp, ())
thread.start_new_thread(serveur_ble, ())
thread.start_new_thread(serveur_lora, ())

# Boucle principale pour maintenir le programme en cours d'exécution
while True:
    time.sleep(1)
