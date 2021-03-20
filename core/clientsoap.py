from zeep import Client

client = None

def init_soap(app):
	global client
	client = Client(app.config['WSDL_SERVER'])
