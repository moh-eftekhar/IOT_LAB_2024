import cherrypy

class HelloWorld:
    exposed = True
    def GET(self,*uri,**params):
        output = "Hello World!"
        if len(uri) != 0:
            output += "<br>uri: " + ',' .join(uri)
        
        if params != {}:
            output += "<br>params: " + ','.join(params)
        
        return output
    
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }

    webService = HelloWorld()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()
