import falcon

class HelloWorld():

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200
        resp.body = 'Hello World.\n'

app = falcon.API()
app.add_route('/', HelloWorld)
