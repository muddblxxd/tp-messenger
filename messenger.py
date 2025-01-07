from datetime import datetime

class User:
    def __init__(self, id:int, name:str):
        self.id = id
        self.name = name
    def __repr__(self) -> str:
        return f'User(id={self.id}, name={self.name})'
    @classmethod
    def from_dict(cls, user_dict: dict) ->'User':
        return cls(user_dict['id'], user_dict['name'])
   
class Client:
    def __init__(self, server) :
        self.server = server

    def connexion(self):
        print('Messenger')
        print('---------')
        print('i. inscription')
        print('c. connexion')
        print('')
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'c':
            mon_id = int(input('Id? :'))
        elif choice == 'i':
            name = input('Ton joli nom ?')
            mon_id = max([user.id for user in self.server.users]) + 1
            self.server.users.append(User(mon_id, name))
            print('ton id c', mon_id)
        else:
            print('Unknown option', choice)
            return self.connexion(self)
        self.choix_menu(mon_id)

    def choix_users(self, mon_id):
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            name = input('Choisir nom :')
            id = max([user.id for user in self.server.users]) + 1
            self.server.users.append(User(id, name))
            print('User list')
            print('---------')
            print('')
            for user in self.server.users:
                print(user.id,'.', user.name)
            print('')
            print('n. Créer un compte')
            print('x. Menu')
            print('')
            self.choix_users(mon_id)
        else :
            self.choix_menu(mon_id)

    def choix_voir_message(self, mon_id, id_groupe):
        for channel in self.server.channels:
            if channel.id == id_groupe:
                name_groupe = channel.name
        print(name_groupe)
        print('------------------')
        for message in self.server.messages :
            if message.channel == id_groupe:
                reception_date = message.reception_date
                sender_id = message.sender_id
                content = message.content
        for user in self.server.users:
            if user.id == sender_id:
                name = user.name
        print(reception_date)
        print(name, ':', content)
        print('')
        print('s. envoyer un message')
        print('x. retour aux menu')
        print('')


    def choix_message(self, mon_id, id_groupe):
        choice = input('enter a choice and press <Enter>:')
        if choice == 'x':
            self.afficher_channels(mon_id)
            self.choix_channels(mon_id)
        elif choice == 's':
            content = input('Tu veux envoyer quoi ? :')
            copy = self.server.messages.copy()
            for mess in copy:
                if id_groupe == mess.channel:
                    id = max([message.id for message in self.server.messages]) + 1
                    reception_date=datetime.now()
                    server.messages.append(Message(id, reception_date, mon_id, id_groupe, content))
            print('')
            print('s. envoyer msg')
            print('x. retour')
            print('')
            self.choix_message(mon_id, id_groupe)
        else :
            print('Unknown option', choice)
            self.choix_message(mon_id, id_groupe)


    def choix_channels(self, mon_id):
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            id = max([channel.id for channel in self.server.channels]) + 1
            name = input('Nom groupe :')
            members_name = (input('Liste amis :'))
            liste_members_name = members_name.split(',')
            liste_members_name_finale = []
            for e in liste_members_name:
                liste_members_name_finale.append(e.strip())
            liste_id = []
            for m in liste_members_name_finale :
                for user in server.users:
                    if user.name == m:
                        liste_id.append(user.id)
            self.server.channels.append(Channel(id, name, liste_id))
            for channel in server.channels:
                print(channel)
            print('')
            print('n. Créer groupe')
            print('a. Ajouter amis')
            print('m. Voir msg')
            print('x. Menu')
            print('')
            self.choix_channels(mon_id)
        elif choice == 'x':
            self.choix_menu(mon_id)
        elif choice == 'a':
            groupe_id = int(input('Id groupe ? :'))
            print('')
            print('Liste amis')
            print('---------')
            print('')
            for user in self.server.users:
                print(user.id,'.', user.name)
            print('')
            member_id = int(input('Id amis :'))
            for channel in self.server.channels:
                if channel.id == groupe_id:
                    channel.member_ids.append(member_id)
            for channel in self.server.channels:
                print(channel)
            print('')
            print('n. Créer un groupe')
            print('a. Ajouter un membre')
            print('x. Menu')
            print('')
            self.choix_channels(mon_id)
        elif choice == 'm':
            id_groupe = int(input('Nom du groupe :'))
            self.choix_voir_message(mon_id, id_groupe)
        else :
            print('Existe pas', choice)
            self.choix_channels(mon_id)
    

    def choix_menu(self, mon_id):
        print('=== Messenger ===')
        print('')
        print('1. Voir amis')
        print('2. Voir groupe')
        print('')
        print('x. Quitter')
        print('')
        choice = input('Select an option: ')
        print('')
        if choice == 'x':
            save_server(self.server)
            print('Bye !')
            return None
        elif choice == '1':
            print('Liste amis')
            print('---------')
            print('')
            for user in self.server.users:
                print(user.id,'.', user.name)
            print('')
            print('n. Créer un compte')
            print('x. Menu')
            print('')
            self.choix_users(mon_id)
        elif choice == '2':
            self.afficher_channels(mon_id)
            self.choix_channels(mon_id)
        else:
            print('Existe pas', choice)
            self.choix_menu(mon_id)

    def afficher_channels(self, mon_id):
        print('Voir groupe')
        print('---------')
        print('')
        has_channel = False
        for channel in self.server.channels:
            if mon_id in channel.member_ids:
                has_channel = True
                id_users = channel.member_ids
                membres = []
                for user in self.server.users:
                    if user.id in id_users:
                        membres.append(user.name)
                print(channel.id,'.', channel.name, ', membres :', [m for m in membres])
        if has_channel:
            print('')
            print('n. Créer un groupe')
            print('a. Ajouter un membre')
            print('m. Voir msg')
            print('x. Menu')
            print('')
        else:
            print('Tapadamis')
            print('')
            print('n. Créer un groupe')
            print('x. Menu')
            print('')

class Channel:
    def __init__(self, id:int, name:str, member_ids:list):
        self.id = id
        self.name = name
        self.member_ids = member_ids
    def __repr__(self) -> str:
        return f'Channel(id={self.id}, name={self.name}, member_ids={self.member_ids})'
    @classmethod
    def from_dict(cls, channel_dict: dict) ->'Channel':
        return cls(channel_dict['id'], channel_dict['name'], channel_dict['member_ids'])
   
class Message:
    def __init__(self, id:int, reception_date:str, sender_id:int, channel:int, content:str):
        self.id = id
        self.reception_date = reception_date
        self.sender_id = sender_id
        self.channel = channel
        self.content = content
    def __repr__(self) -> str:
        return f'Message(id={self.id}, reception_date={self.reception_date}, sender_id={self.sender_id}, channel={self.channel}, content={self.content})'
    @classmethod
    def from_dict(cls, message_dict: dict) ->'Message':
        return cls(message_dict['id'], message_dict['reception_date'], message_dict['sender_id'], message_dict['channel'], message_dict['content'])

class Server:
    def __init__(self, users:list[User], channels:list[Channel], messages:list[Message]):
        self.users = users
        self.channels = channels
        self.messages = messages
    def __repr__(self) -> str:
        return f'Server(users={self.users}, channels={self.channels}, messages=[{self.messages}])'
    @classmethod
    def from_dict(cls, server_dict : dict) -> 'Server':
        new_server = Server([], [], [])
        for user in server_dict['users'] :
            new_server.users.append(User.from_dict(user))
        for channel in server_dict['channels'] :
            new_server.channels.append(Channel.from_dict(channel))
        for message in server_dict['messages'] :
            new_server.messages.append(Message.from_dict(message))
        return new_server
   
server1 = { "users": [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ],
    "channels": [
        {"id": 1, "name": "Town square", "member_ids": [1, 2]}
    ],
    "messages": [
        {
            "id": 1,
            "reception_date": "07/11/2024, 11:06",
            "sender_id": 1,
            "channel": 1,
            "content": "Hi"
        }
    ]}


import json
SERVER_FILE_NAME = 'serverdata.json'

with open(SERVER_FILE_NAME) as fichier:
    server = json.load(fichier)


server = Server.from_dict(server)

def save_server(server_to_save : Server):
    new_server = {'users':[], 'channels':[], 'messages':[]}
    for user in server_to_save.users :
        new_server['users'].append({'id': user.id, 'name':user.name} )
    for channel in server_to_save.channels :
        new_server['channels'].append({'id' : channel.id, 'name' : channel.name, 'member_ids':channel.member_ids})
    for message in server_to_save.messages :
        new_server['messages'].append({'id':message.id, 'reception_date':message.reception_date, 'sender_id' : message.sender_id, 'channel':message.channel, 'content':message.content})
    with open(SERVER_FILE_NAME, "w") as file :
        json.dump(new_server, file)
    return new_server


# def connexion():
#     print('Messenger')
#     print('---------')
#     print('i. inscription')
#     print('c. connexion')
#     print('')
#     choice = input('Enter a choice and press <Enter>:')
#     if choice == 'c':
#         mon_id = int(input('Id? :'))
#     elif choice == 'i':
#         name = input('Ton joli nom ?')
#         mon_id = max([user.id for user in server.users]) + 1
#         server.users.append(User(mon_id, name))
#         print('ton id c', mon_id)
#     else:
#         print('Unknown option', choice)
#         return connexion()
#     choix_menu(mon_id)

# def choix_users(mon_id):
#     choice = input('Enter a choice and press <Enter>:')
#     if choice == 'n':
#         name = input('Choisir nom :')
#         id = max([user.id for user in server.users]) + 1
#         server.users.append(User(id, name))
#         print('User list')
#         print('---------')
#         print('')
#         for user in server.users:
#             print(user.id,'.', user.name)
#         print('')
#         print('n. Créer un compte')
#         print('x. Menu')
#         print('')
#         choix_users(mon_id)
#     else :
#         choix_menu(mon_id)

# def choix_voir_message(mon_id, id_groupe):
#     for channel in server.channels:
#         if channel.id == id_groupe:
#             name_groupe = channel.name
#     print(name_groupe)
#     print('------------------')
#     for message in server.messages :
#         if message.channel == id_groupe:
#             reception_date = message.reception_date
#             sender_id = message.sender_id
#             content = message.content
#     for user in server.users:
#         if user.id == sender_id:
#             name = user.name
#     print(reception_date)
#     print(name, ':', content)
#     print('')
#     print('s. envoyer un message')
#     print('x. retour aux menu')
#     print('')


# def choix_message(mon_id, id_groupe):
#     choice = input('enter a choice and press <Enter>:')
#     if choice == 'x':
#         afficher_channels(mon_id)
#         choix_channels(mon_id)
#     elif choice == 's':
#         content = input('Tu veux envoyer quoi ? :')
#         copy = server.messages.copy()
#         for mess in copy:
#             if id_groupe == mess.channel:
#                 id = max([message.id for message in server.messages]) + 1
#                 reception_date=datetime.now()
#                 server.messages.append(Message(id, reception_date, mon_id, id_groupe, content))
#         print('')
#         print('s. envoyer msg')
#         print('x. retour')
#         print('')
#         choix_message(mon_id, id_groupe)
#     else :
#         print('Unknown option', choice)
#         choix_message(mon_id, id_groupe)


# def choix_channels(mon_id):
#     choice = input('Enter a choice and press <Enter>:')
#     if choice == 'n':
#         id = max([channel.id for channel in server.channels]) + 1
#         name = input('Nom groupe :')
#         members_name = (input('Liste amis :'))
#         liste_members_name = members_name.split(',')
#         liste_members_name_finale = []
#         for e in liste_members_name:
#             liste_members_name_finale.append(e.strip())
#         liste_id = []
#         for m in liste_members_name_finale :
#             for user in server.users:
#                 if user.name == m:
#                     liste_id.append(user.id)
#         server.channels.append(Channel(id, name, liste_id))
#         for channel in server.channels:
#             print(channel)
#         print('')
#         print('n. Créer groupe')
#         print('a. Ajouter amis')
#         print('m. Voir msg')
#         print('x. Menu')
#         print('')
#         choix_channels(mon_id)
#     elif choice == 'x':
#         choix_menu(mon_id)
#     elif choice == 'a':
#         groupe_id = int(input('Id groupe ? :'))
#         print('')
#         print('Liste amis')
#         print('---------')
#         print('')
#         for user in server.users:
#             print(user.id,'.', user.name)
#         print('')
#         member_id = int(input('Id amis :'))
#         for channel in server.channels:
#             if channel.id == groupe_id:
#                 channel.member_ids.append(member_id)
#         for channel in server.channels:
#             print(channel)
#         print('')
#         print('n. Créer un groupe')
#         print('a. Ajouter un membre')
#         print('x. Menu')
#         print('')
#         choix_channels(mon_id)
#     elif choice == 'm':
#         id_groupe = int(input('Nom du groupe :'))
#         choix_voir_message(mon_id, id_groupe)
#     else :
#         print('Existe pas', choice)
#         choix_channels(mon_id)
   

# def choix_menu(mon_id):
#     print('=== Messenger ===')
#     print('')
#     print('1. Voir amis')
#     print('2. Voir groupe')
#     print('')
#     print('x. Quitter')
#     print('')
#     choice = input('Select an option: ')
#     print('')
#     if choice == 'x':
#         save_server(server)
#         print('Bye !')
#         return None
#     elif choice == '1':
#         print('Liste amis')
#         print('---------')
#         print('')
#         for user in server.users:
#             print(user.id,'.', user.name)
#         print('')
#         print('n. Créer un compte')
#         print('x. Menu')
#         print('')
#         choix_users(mon_id)
#     elif choice == '2':
#         afficher_channels(mon_id)
#         choix_channels(mon_id)
#     else:
#         print('Existe pas', choice)
#         choix_menu(mon_id)

# def afficher_channels(mon_id):
#     print('Voir groupe')
#     print('---------')
#     print('')
#     has_channel = False
#     for channel in server.channels:
#         if mon_id in channel.member_ids:
#             has_channel = True
#             id_users = channel.member_ids
#             membres = []
#             for user in server.users:
#                 if user.id in id_users:
#                     membres.append(user.name)
#             print(channel.id,'.', channel.name, ', membres :', [m for m in membres])
#     if has_channel:
#         print('')
#         print('n. Créer un groupe')
#         print('a. Ajouter un membre')
#         print('m. Voir msg')
#         print('x. Menu')
#         print('')
#     else:
#         print('Tapadamis')
#         print('')
#         print('n. Créer un groupe')
#         print('x. Menu')
#         print('')

client = Client(server)

client.connexion()
