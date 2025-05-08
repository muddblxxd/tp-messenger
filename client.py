from datetime import datetime
# Il vaut mieux éviter les `import *`, car ça importera automatiquement tous les éléments que vous rajouterez par la suite dans les fichiers concernés. Vous risquez alors des conflits de nommage entre plusieurs fichiers.
from server import Server
from model import Channel, Message, User
from remoteServer import RemoteServer

class Client:
    # Vous pouvez indiquer que votre variable `server` est soit
    # du type `Server`, soit du type `RemoteServer`
    def __init__(self, server: RemoteServer | Server) :
        self.server = server

    def connexion(self) -> None:
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
            # La gestion des identifiants se fait plutôt
            # côté serveur. Il vaut donc mieux définir une fonction `add_user`
            # dans `Server` comme vous l'avez fait dans `RemoteServer`.
            # Cet appel choisira ensuite la bonne fonction.
            me = self.server.add_user(name)
            mon_id = me.id

            print('ton id c', mon_id)
        else:
            print('Existe pas', choice)
            # Vous n'avez pas besoin de passer `self` en argument :
            # Python le fait automatiquement pour les fonctions
            # définies dans des classes.
            return self.connexion()
        self.choix_menu(mon_id)

    def choix_users(self, mon_id):
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            name = input('Choisir nom :')
            # Il vaut mieux utiliser les fonctions des seveurs
            self.server.add_user(name)
            print('Liste utilisateur23')
            print('---------')
            print('')
            for user in self.server.users():
                print(user.id,'.', user.name)
            print('')
            print('n. Créer un compte')
            print('x. Menu')
            print('')
            self.choix_users(mon_id)
        else :
            self.choix_menu(mon_id)

    def choix_voir_message(self, mon_id: int, id_groupe: int) -> None:
        for channel in self.server.channels():
            if channel.id == id_groupe:
                name_groupe = channel.name
        print(name_groupe)
        print('------------------')
        for message in self.server.messages():
            if message.channel == id_groupe:
                reception_date = message.reception_date
                sender_id = message.sender_id
                content = message.content
        # Attention, comme vous n'aviez pas inclus cette boucle
        # dans l'autre, seul un message s'affichait
                for user in self.server.users():
                    if user.id == sender_id:
                        name = user.name
                print(reception_date)
                print(name, ':', content)
                print('')
                print('s. envoyer un message')
                print('x. retour aux menu')
                print('')


    def choix_message(self, mon_id: int, id_groupe: int) -> None:
        choice = input('enter a choice and press <Enter>:')
        if choice == 'x':
            self.afficher_channels(mon_id)
            self.choix_channels(mon_id)
        elif choice == 's':
            content = input('Tu veux envoyer quoi ? :')
            copy = self.server.messages().copy()
            # Pourquoi itérez-vous sur tous les messages ?
            # Avec ce code, vous allez créer un nouveau message
            # par message déjà existant dans le groupe.
            # Vous n'avez pas besoin de boucle : vous avez déjà
            # tout ce dont vous avez besoin pour appeler une
            # nouvelle fonction `server.send_message` qui s'occupera
            # de créer l'objet `Message`.
            for mess in copy:
                if id_groupe == mess.channel:
                    id = max([message.id for message in self.server.messages()]) + 1
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


    def choix_channels(self, mon_id: int) -> None:
        choice = input('Enter a choice and press <Enter>:')
        if choice == 'n':
            id = max([channel.id for channel in self.server.channels()]) + 1
            name = input('Nom groupe :')
            members_name = (input('Liste amis :'))
            liste_members_name = members_name.split(',')
            liste_members_name_finale = []
            for e in liste_members_name:
                liste_members_name_finale.append(e.strip())
            liste_id = []
            for m in liste_members_name_finale :
                for user in self.server.users():
                    if user.name == m:
                        liste_id.append(user.id)
            # Comme pour les users, il vaut mieux créer des fonctions
            # `Server.add_channel` et `RemoteServer.add_channel`,
            # et se contenter d'appeler `server.add_channel` ici.
            self.server.channels.append(Channel(id, name, liste_id))
            for channel in self.server.channels:
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
            for user in self.server.users():
                print(user.id,'.', user.name)
            print('')
            member_id = int(input('Id amis :'))
            for channel in self.server.channels():
                if channel.id == groupe_id:
                    # Il vaut mieux créer des fonctions `add_channel_member`
                    # côté serveur.
                    channel.member_ids.append(member_id)
            for channel in self.server.channels():
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
    

    def choix_menu(self, mon_id: int) -> None:
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
            # Il vaut mieux n'appeler `save_server` que depuis
            # l'intérieur des fonctions de `Server`, car cette fonction
            # n'a pas de sens pour un `RemoteServer`
            # Par ailleurs il est préférable de l'appeler dès que
            # vous avez des données à sauvegarder, et pas juste à la fin.
            print('Bye !')
            return None
        elif choice == '1':
            print('Liste amis')
            print('---------')
            print('')
            for user in self.server.users():
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

    def afficher_channels(self, mon_id: int) -> None:
        print('Voir groupe')
        print('---------')
        print('')
        has_channel = False
        # Il faut implémenter la méthode `channels`
        # dans les classes `Server` et `RemoteServer`
        for channel in self.server.channels():
            if mon_id in channel.member_ids:
                has_channel = True
                id_users = channel.member_ids
                membres = []
                for user in self.server.users():
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

