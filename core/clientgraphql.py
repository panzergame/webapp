from Singleton import Singleton
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

class ClientGraphQl(Client, metaclass=Singleton):
    def __init__(self):
        transport = RequestsHTTPTransport(url='http://127.0.0.1:5000/graphql', use_json=True) # TODO config
        Client.__init__(self, transport=transport, fetch_schema_from_transport=True)
