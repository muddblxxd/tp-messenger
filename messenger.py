from datetime import datetime

server = {
    'users': [
        {'id': 1, 'name': 'Lise'},
        {'id': 2, 'name': 'bgdu65'}
    ],
    'channels': [
        {'id': 1, 'name': 'Groupe 5 info', 'member_ids': [1, 2]}
    ],
    'messages': [
        {
            'id': 1,
            'reception_date': datetime.now(),
            'sender_id': 1,
            'channel': 1,
            'content': 'Hi 👋'
        }
    ]
}

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

    print('m. Retour au menu')

def crea(serv) :
    nom = input('Quel est ton jolie petit nom ? ')
    k = len(server['users'])+1
    server['users'].append({'id': k, 'name' : nom})
    menu(server)

def creag(serv) :
    nom = input('Quel est le nom de ton groupe ? ')
    t=len(server['channels'])+1
    c=''
    while c != 'Non':
        n = input(' Quel est le nom du nouveau membre du groupe ? ')
        server['channels'].append({'id' : t, 'name' : nom, 'member_ids' : []})
        k=1
        while server['users'][k]['name'] != n :
            k=k+1
            server['channels'][t]['name'][nom]['member_ids'] = k
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
        print('Bye!')
    elif choice == 'm':
        menu(server)
    elif choice == 'g' :
        creag(server)
    else : 
        print('Unknown option:', choice)


