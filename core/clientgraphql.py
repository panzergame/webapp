from gql import Client
from gql.transport.requests import RequestsHTTPTransport

clientql = None

def init_graphql(app):
	global clientql

	transport = RequestsHTTPTransport(url=app.config['GRAPHQL_SERVER'], use_json=True)
	clientql = Client(transport=transport, fetch_schema_from_transport=True)
