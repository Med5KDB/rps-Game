# Importation du module socket
import socket
import argparse


bind_HOST = 'localhost'
# bind_PORT = 8080

# Arguments Managing
parser = argparse.ArgumentParser()
# Use of add_argument pour specifier le nom et les caracteristiques d'un argument 
parser.add_argument("--base", required=True, help="Path to the directory of The Website hosted by the Server")
parser.add_argument("--port", required=True, help="The Server listening PORT", type=int)
arguments = parser.parse_args()


response = "HTTP/1.1 200 OK\nContent-Type:text/html;charset=utf-8\n\n"

# content_length = len(response)
# response+= f"Content-Length:{content_length}\n\n"

noGET_response = "HTTP/1.1 501 Not Implemented\nContent-Type:text/html\n\n"
noGET_response += "<html><body>The requested method is not implemented on the server.</body></html>"

notFound_response = "HTTP/1.1 404 Not Found\nContent-Type:text/html\n\n<html><body>Error 404: Not Found.</body></html>"
# noGetresp_length = len(noGET_response)
# noGET_response+= f"Content-Length:{noGetresp_length}\n\n"

# Faut savoir que le decode() ne peut pas etre uilise que pour les chaines de caracteres utf-8

# On envoie que le fichier HTML
with open(arguments.base,'rb') as monSite:
    response+=  monSite.read().decode()  # On ajoute notre fichier html au response

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((bind_HOST, arguments.port))
    server.listen()
    print("The server is  listening on %s:%d" %(bind_HOST, arguments.port))
    print("And is waiting for a connection")
    connection, addresse = server.accept()
    with connection:
        print('Connection established by ', addresse)
        while True:
            data = connection.recv(1024)
            request = data.split()[0]
            print("Request: ", request.decode())
            if request.decode() == "POST" :
                print("Damn!!! No GET request\n")
                connection.sendall(noGET_response.encode())
                break
            if request.decode() == "GET":
                print("Received:",data)
                connection.sendall(response.encode())
            else:
                print("Error 404:Not Found\n")
                connection.sendall(notFound_response.encode())
                
    # A t on reellement besoin de fermer la connexion du client ???
    # Non grace au mot cle with
    connection.close()
# server.close()

# Pas la peine de fermer le socket du serveur car nous avons utilise le mot-cle with : server.close()

#  La boucle while permet au serveur de rester en attente de nouvelles connexions 
#  et de traiter les données envoyées par les clients de manière itérative.

# La methode accept de la classe "socket" permet de mettre en attente le serveur
# Lorsqu'un client se connecte, la méthode retourne une nouvelle socket qui peut être utilisée pour envoyer 
# et recevoir des données ainsi que l'adresse IP et le numéro de port du client.

# Pour niom SAER je peux mettre client_socket, client_address = server.accept()