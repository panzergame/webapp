from flask_login import UserMixin
import mangopay

mangopay.client_id = 'testclient1' # TODO config
mangopay.apikey = 'iv8f2ueKUBrAFau3whegoXJzRk1ZVUOfBLQSvrGoWpJy5VmoYj'

from mangopay.api import APIRequest
from mangopay.resources import *
from mangopay.utils import Address

class Client(UserMixin):
    def __init__(self, id, username, email, password, mangopayid=None):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        
        if mangopayid:
            self.__mangopay_user = Client.get(mangopayid)

    def register_mangopay(self, firstname, lastname, birthday, nationality, country_of_residence):
        self.__mangopay_user = NaturalUser(first_name=firstname,
                           last_name=lastname,
                           birthday=birthday,
                           nationality=nationality,
                           country_of_residence=country_of_residence,
                           email=self.email)
        self.__mangopay_user.save()

        self.save()

    @staticmethod
    def create(username, email, password):
        user = Client(0, username, email, password) # TODO id
        user.save()

    @staticmethod
    def get(id):
        return Client(id, 'toto', 'toto@mail.com', 'toto')

    @staticmethod
    def get_by_credential(email, password):
        return Client(0, 'toto', email, password)

    def save(self):
        pass
