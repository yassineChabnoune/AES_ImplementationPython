import socket, pickle
from bedPatientData import bedData

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

def send(obj):

    data_string = pickle.dumps(obj)
    client.sendall(data_string)
    

try:

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    variable = bedData()
    send(variable)
    send(DISCONNECT_MESSAGE)


except ConnectionRefusedError:

    print("echec de la connexion ")

except:

    print("erreur !!!")

finally:

    client.close()










