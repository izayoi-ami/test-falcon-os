import falcon

class HelloWorld():

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hello World.\n'

api = application = falcon.API()
api.add_route('/', HelloWorld())
