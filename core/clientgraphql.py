from gql import Client
from gql.transport.requests import RequestsHTTPTransport

client = None

def init_graphql(app):
	global client

	transport = RequestsHTTPTransport(url=app.config['GRAPHQL_SERVER'], use_json=True)
	client = Client(transport=transport, fetch_schema_from_transport=True)
