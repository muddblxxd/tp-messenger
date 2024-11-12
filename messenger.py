from datetime import datetime
import json 

with open('serverdata.json') as file :
    server = json.load(file)

#name=[]
# for user in server['user'] :
#     name.append(user['name'])

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
        return crea(server)
    elif choice == 'm':
        return menu(server)
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
        return aff(server)
    elif choice == 'm':
        return menu(server)
    else:
        print('Choix inconnu :(')
        return channels(serv)

def aff(serv) :
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
        return users(server)
    elif choice == '2':
        return channels(server)
    elif choice == 'n' :
        return crea(server)
    elif choice == 'x':
        sauv(server)
        print('Bye!')
        return
    elif choice == 'g' :
        return creag(server)
    else : 
        print('Unknown option:', choice)
        return menu(serv)

def sauv(serv) :
    with open('serverdata.json', "w") as file :
            json.dump(serv, file)

menu(server)
