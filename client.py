from datetime import datetime
from server import *
from model import *
from remoteServer import *

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
            mon_id = max([user.id for user in self.server.users()]) + 1
            self.server.add_user(name)

            print('ton id c', mon_id)
        else:
            print('Existe pas', choice)
            return self.connexion(self)
        self.choix_menu(mon_id)

    def choix_users(self, mon_id):
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            name = input('Choisir nom :')
            id = max([user.id for user in self.server.users]) + 1
            self.server.users.append(User(id, name))
            print('Liste utilisateur23')
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

