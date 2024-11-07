import cherrypy
import json

class Webcalculator:
    exposed = True
    def __init__(self):
        pass
    
    def GET(self,*uri,**params):
        output = ""
        if len(uri) > 0:
            operation = uri[0]
            operand = []
            if params != {}:
                for key in params.keys():
                    operand.append(params[key])
            if len(operand) > 0:
                i=0
                for i in range(len(operand)):
                    operand[i] = int(operand[i])
            if operation == "add":
                text_to_return=self.add(operation,operand)
                return text_to_return

    def add(self,operation,operand):
        print("operand: ",operand)
        result = operand[0] + operand[1]
        result_json = {"operation": operation, "operands": operand, "result": result}
        return json.dumps(result_json, indent=4)
        
    
if __name__ == '__main__':
    conf = {
        '/': {
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True
        }
    }

    webService = Webcalculator()
    cherrypy.tree.mount(webService, '/', conf)
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()