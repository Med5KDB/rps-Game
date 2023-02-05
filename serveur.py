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


response = ""
css_response = "HTTP/1.1 200 OK\nContent-Type:text/css\n\n"
# content_length = len(response)
# response+= f"Content-Length:{content_length}\n\n"

noGET_response = "HTTP/1.1 501 Not Implemented\nContent-Type:text/html\n\n"
noGET_response += "<html><body>The requested method is not implemented on the server.</body></html>"

notFound_response = "HTTP/1.1 404 Not Found\nContent-Type:text/html\n\n<html><body>Error 404: Not Found.</body></html>"

# Faut savoir que le decode() ne peut pas etre uilise que pour les chaines de caracteres utf-8

# On envoie que le fichier HTML
# with open(arguments.base,'rb') as monSite:
#     response+=  monSite.read().decode()  # On ajoute notre fichier html au response

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# On lie le socket a une @IP et a un Port
server.bind((bind_HOST, arguments.port))
server.listen()
print("The server is  listening on %s:%d" %(bind_HOST, arguments.port))
print("And is waiting for a connection")
while True:
    connection, addresse = server.accept()
    with connection:
        print('Connection established with the client by ', addresse)
        # Reception des donnees du client
        data = connection.recv(1024)
        request = data.split()[0]
        print("Les donnees envoyees par le navigateur: ",data)
        print("Request: ", request.decode())
        
        # Recuperation de la ressource sent by the client(browser)
        resource = data.split()[1]
        print("Ressource: "+resource.decode())

        if ".css" in data.decode():
            with open("calc.css", "r") as file:
                res = file.read()
                connection.send(css_response.encode())
                connection.send(res.encode())
            
        # elif ".js" in data.decode():
        #     with open("calc.js", "r") as file:
        #         res = file.read()
        else:
            with open(arguments.base, 'r') as file:
                res = file.read()
                connection.send('HTTP/1.1 200 OK\nContent-Type:text/html;charset=utf-8\n\n'.encode())
                connection.send(res.encode())
    
    
    # connection.send(res.encode())
    connection.close()

    # page = """
    #     <html>
    #         <head>
    #             <link rel="stylesheet" type="text/css" href="style.css">
    #             <script src="script.js"></script>
    #         </head>
    #         <body>
    #             <h1>Bienvenue sur notre site</h1>
    #             <p>Ceci est une page HTML envoyée par le serveur</p>
    #         </body>
    #     </html>
    #     """
    

    # if request.decode() != "GET" :
    #     print("Damn!!! No GET request\n")
    #     connection.sendall(noGET_response.encode())
    # if request.decode() == "GET":
    #     if resource.decode() == '/':
    #         try:
    #             file = open(arguments.base, 'r')
    #             html_content = file.read()
    #             # response+= html_content
    #             # response += '<link rel="stylesheet" type="text/css" href="calc.css">'
    #             # Envoi de la reponse html
    #             # print("Received:",data)
    #             connection.send('HTTP/1.1 200 OK\nContent-Type:text/html;charset=utf-8\n\n'.encode())
    #             connection.send('<link rel="stylesheet" type="text/css" href="calc.css">'.encode())
    #             connection.send(html_content.encode())
    #             connection.sendall(response.encode())
    #             print("The HTML file is sent")
    #             # with open("calc.css", 'r') as css_file:
    #             #     css_content = css_file.read()
    #             #     css_response += css_content
    #             #     connection.sendall(css_response.encode())
    #             #     print("The CSS file is sent")
    #         except IOError:
    #             # Envoi de la reponse HTTP pour indiquer que le fichier html est introuvable
    #             print("Error 404:Not Found\n")
    #             connection.sendall(notFound_response.encode())
        # elif resource.decode() == '/calc.css':
        #     try:
        #         with open("calc.css", 'r') as css_file:
        #             css_content = css_file.read()
        #             css_response = "HTTP/1.1 200 OK\nContent-Type:text/css\n\n"
        #             css_response += css_content
        #             # Envoi de la réponse css
        #             connection.sendall(css_response.encode())
        #             print("The CSS file is sent")
        #     except IOError:
        #         # Envoi de la réponse HTTP pour indiquer que le fichier css est introuvable
        #         print("Error 404:Not Found\n")
        #         connection.sendall(notFound_response.encode())
                #  
                # with open(resource[1:], 'r') as file:
                    
        
                
                
    # A t on reellement besoin de fermer la connexion du client ???
    # Non grace au mot cle with
    # connection.close()
# server.close()

# Pas la peine de fermer le socket du serveur car nous avons utilise le mot-cle with : server.close()

#  La boucle while permet au serveur de rester en attente de nouvelles connexions 
#  et de traiter les données envoyées par les clients de manière itérative.

# La methode accept de la classe "socket" permet de mettre en attente le serveur
# Lorsqu'un client se connecte, la méthode retourne une nouvelle socket qui peut être utilisée pour envoyer 
# et recevoir des données ainsi que l'adresse IP et le numéro de port du client.

# Pour niom SAER je peux mettre client_socket, client_address = server.accept()