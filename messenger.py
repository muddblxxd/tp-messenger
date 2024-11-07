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
    n = len(server['users'])
    for k in range(n) :
        print(server['users'][k]['id'],server['users'][k]['name'])
    print('')
    print('n. Créer ton id')
    print('m. Retour au menu')
    
        
def channels(serv) :
    print(' ~~~~~ Nom du groupe ~~~~~')
    print('')
    m = len(server['channels'])
    for p in range(m) :
        print(server['channels'][p]['name'])
        print('')
    print('h. Afficher les membres d un groupes')
    print('m. Retour au menu')

def aff(serv) :
    name=input('Quelle groupe ? ')
    
    

def crea(serv) :
    nom = input('Quel est ton jolie petit nom ? ')
    k = len(server['users'])+1
    server['users'].append({'id': k, 'name' : nom})
    menu(server)

def creag(serv) :
    nom = input('Quel est le nom de ton groupe ? ')
    t=len(server['channels'])+1
    c='g'
    l=[]
    while c != 'Non':
        n = input('Quel est le nom du nouveau membre du groupe ? ')
        p=0
        while server['users'][p]['name'] != n :
            p=p+1
        l.append(p+1)    
        server['channels'].append({'id' : t, 'name' : nom, 'member_ids' : l })
        c = input('Voulez vous ajouter d autres membres ?')
    menu(server)

def menu(serv) :
    print('=== Messenger ===')
    print('1. Voir les copains')
    print('2. Voir les groupes')
    print('')
    print('n. Créer ton id')
    print('g. Créer un nouveau groupe')
    print('x. Quitter l appli')

def sauv(serv) :
    with open('serverdata.json', "w") as file :
            json.dump(server, file)

choice = ''
menu(server)
while choice != 'x' :
    choice = input('Faites un choix ! : ')
    if choice == '1':
        users(server)
    elif choice == '2':
        channels(server)
    elif choice == 'n' :
        crea(server)
    elif choice == 'x':
        sauv(server)
        print('Bye!')
    elif choice == 'm':
        menu(server)
    elif choice == 'g' :
        creag(server)
    elif choice == 'h' :
        aff(server)
    else : 
        print('Unknown option:', choice)


