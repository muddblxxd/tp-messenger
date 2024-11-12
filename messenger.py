from datetime import datetime
import json 

# with open('serverdata.json') as file :
#     server = json.load(file)

SERVER_FILE_NAME = 'serverdata.json'
def load_server():
    with open(SERVER_FILE_NAME) as json_file :
        serv= json.load(json_file)

serv = load_server()

def save_server(server_to_save : dict):
    json.dump(server_to_save, open(SERVER_FILE_NAME, 'w'))

class User :
    def __init__(self, id: int, name: str)
        self.id = id
        self.name = name

class Channel :
    def __init__(self,id: int, name:str, member_ids: list) :
        self.id = id
        self.name = name
        self.member_ids = member_ids

def users(serv) :
    print(' ---- Listes des copains ----')
    print('')
    n = len(serv['users'])
    for k in range(n) :
        print(serv['users'][k]['id'],serv['users'][k]['name'])
    print('')
    print('n. Créer ton id')
    print('m. Retour au menu')
    choice = input('Faites un choix ! : ')
    if choice == 'n' :
        return crea(serv)
    elif choice == 'm':
        return menu(serv)
    else:
        print('Choix inconnu :(')
        return users(serv)
  
def channels(serv) :
    print(' ~~~~~ Nom du groupe ~~~~~')
    print('')
    m = len(serv['channels'])
    for p in range(m) :
        print(serv['channels'][p]['name'])
        print('')
    print('h. Afficher les membres d un groupes')
    print('m. Retour au menu')
    choice = input('Faites un choix ! : ')
    if choice == 'h' :
        return affichage(serv)
    elif choice == 'm':
        return menu(serv)
    else:
        print('Choix inconnu :(')
        return channels(serv)

def affichage(serv) :
    name=input('Quelle groupe ? ')
    
def crea(serv) :
    nom = input('Quel est ton jolie petit nom ? ')
    k = len(serv['users'])+1
    serv['users'].append({'id': k, 'name' : nom})
    menu(serv)

def creag(serv) :
    nom = input('Quel est le nom de ton groupe ? ')
    t=len(serv['channels'])+1
    c='g'
    l=[]
    while c != 'Non':
        n = input('Quel est le nom du nouveau membre du groupe ? ')
        p=0
        while serv['users'][p]['name'] != n :
            p=p+1
        l.append(p+1)    
        serv['channels'].append({'id' : t, 'name' : nom, 'member_ids' : l })
        c = input('Voulez vous ajouter d autres membres ?')
    menu(serv)

def menu(serv) :
    print('=== Messenger ===')
    print('1. Voir les copains')
    print('2. Voir les groupes')
    print('')
    print('n. Créer ton id')
    print('g. Créer un nouveau groupe')
    print('x. Quitter l appli')
    choice = input('Faites un choix ! : ')
    if choice == '1':
        return users(serv)
    elif choice == '2':
        return channels(serv)
    elif choice == 'n' :
        return crea(serv)
    elif choice == 'x':
        sauv(serv)
        print('Bye!')
        return
    elif choice == 'g' :
        return creag(serv)
    else : 
        print('Unknown option:', choice)
        return menu(serv)

def sauv(serv) :
    with open('serverdata.json', "w") as file :
            json.dump(serv, file)

menu(serv)
