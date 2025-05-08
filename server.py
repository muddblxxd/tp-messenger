import json 
from model import User, Channel, Message 
from client import *

class Server:
    # N'oubliez pas de typer vos paramètres. Pour une liste, la valeur
    # par défaut est plutôt la liste vide que le valeur `None`.
    # Utilisez la liste vide par défaut vous permet de simplifier le
    # remplissage des attributs de `self`
    def __init__(self, filename:str, users: 'list[User]' = [], channels: 'list[Channel]' = [], messages: 'list[Message]' = []):
        self.filename = filename
        # Dans `RemoteServer`, `users` est une fonction qui renvoie
        # une liste d'utilisateur. Ici, c'est une liste d'utilisateurs.
        # Pour garder une cohérence entre les 2 classes, il vaut mieux
        # créer une fonction `users` ici.
        # Pour ne pas avoir de conflit de nommage avec cette variable,
        # on peut la préfixer par un `_`. Ceci indique aux développeurs
        # qu'il ne faut pas accéder directement  à cette variable en dehors
        # des fonctions de cette classe.
        self._users = users
        self._channels = channels
        self._messages = messages

    @classmethod
    def from_dict(cls, filename: str, data: dict) -> 'Server':
        users = [User.from_dict(u) for u in data['users']]
        channels = [Channel.from_dict(c) for c in data['channels']]
        messages = [Message.from_dict(m) for m in data['messages']]
        return cls(filename, users, channels, messages)

    def to_dict(self) -> dict:
        # Vous n'avez pas défini de fonctions `to_dict` dans les classes
        # `User`, `Channel`, et `Message`.
        return {
            'users': [user.to_dict() for user in self._users],
            'channels': [channel.to_dict() for channel in self._channels],
            'messages': [message.to_dict() for message in self._messages]
        }

    def save_to_file(self) -> None:
        """Enregistre l'état actuel du serveur dans un fichier JSON."""
        with open(self.filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'Server':
        """Charge les données du serveur à partir d'un fichier JSON."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
            return cls.from_dict(filename, data)
        except FileNotFoundError:
            print(f"{filename} not found. Aborting.")
            exit(-1)

    def users(self) -> list[User]:
        return self._users

    # Remarquez que cette nouvelle fonction a la même signature
    # (c'est à dire le même nombre et le même type de paramètres et
    # de valeurs de retours) que la fonction `RemoteServer.add_user`.
    # Ca vous permet d'utiliser la fonction `add_user` depuis votre
    # `Client` sans avoir à vous préoccuper de savoir si vous
    # manipulez un `Server` ou un `RemoteServer`
    def add_user(self, name: str) -> User:
        new_id = max([user.id for user in self._users]) + 1
        new_user = User(new_id, name)
        self._users.append(new_user)
        self.save_to_file()

        return new_user
