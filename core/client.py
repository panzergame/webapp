import mangopay

mangopay.client_id = 'testclient1' # TODO config
mangopay.apikey = 'iv8f2ueKUBrAFau3whegoXJzRk1ZVUOfBLQSvrGoWpJy5VmoYj'

from mangopay.api import APIRequest
from mangopay.resources import *
from mangopay.utils import Address

class User:
    def __init__(self, username, email, password, mangopayid=None):
        self.username = username
        self.email = email
        self.password = password
        
        if mangopayid:
            self.__mangopay_user = User.get(mangopayid)

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
        user = User(username, email, password)
        user.save()

    @staticmethod
    def get(id):
        pass

    def save(self):
        pass
