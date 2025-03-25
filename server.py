import json 
from model import User, Channel, Message 
from client import *

class Server:
    SERVER_FILE_NAME = 'serverdata.json'

    def __init__(self, users=None, channels=None, messages=None):
        self.users = users if users else []
        self.channels = channels if channels else []
        self.messages = messages if messages else []

    @classmethod
    def from_dict(cls, data):
        users = [User.from_dict(u) for u in data['users']]
        channels = [Channel.from_dict(c) for c in data['channels']]
        messages = [Message.from_dict(m) for m in data['messages']]
        return cls(users, channels, messages)

    def to_dict(self):
        return {
            'users': [user.to_dict() for user in self.users],
            'channels': [channel.to_dict() for channel in self.channels],
            'messages': [message.to_dict() for message in self.messages]
        }

    def save_to_file(self):
        """Enregistre l'état actuel du serveur dans un fichier JSON."""
        with open(self.SERVER_FILE_NAME, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    @classmethod
    def load_from_file(cls):
        """Charge les données du serveur à partir d'un fichier JSON."""
        try:
            with open(cls.SERVER_FILE_NAME, 'r') as file:
                data = json.load(file)
            return cls.from_dict(data)
        except FileNotFoundError:
            print(f"{cls.SERVER_FILE_NAME} not found. Using default data.")
            return cls()

