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
                    operand[i] = float(operand[i])
            if operation == "add":
                text_to_return=self.add(operation,operand)
                return text_to_return
            elif operation == "sub":
                text_to_return=self.sub(operation,operand)
                return text_to_return
            elif operation == "mul":
                text_to_return=self.mul(operation,operand)
                return text_to_return
            elif operation == "div":
                text_to_return=self.div(operation,operand)
                return text_to_return

    def add(self,operation,operand):
        for i in range(len(operand)):
            if i == 0:
                result = operand[i]
            else:
                result += operand[i]
        result_json = {"operation": operation, "operands": operand, "result": result}
        return json.dumps(result_json, indent=4)
    
    def sub(self,operation,operand):
        for i in range(len(operand)):
            if i == 0:
                result = operand[i]
            else:
                result -= operand[i]
        result_json = {"operation": operation, "operands": operand, "result": result}
        return json.dumps(result_json, indent=4)
    
    def mul(self,operation,operand):
        for i in range(len(operand)):
            if i == 0:
                result = operand[i]
            else:
                result *= operand[i]
        result_json = {"operation": operation, "operands": operand, "result": result}
        return json.dumps(result_json, indent=4)
    
    def div(self,operation,operand):
        for i in range(len(operand)):
            if i == 0:
                result = operand[i]
            else:
                if operand[i] == 0:
                    result = "Division by zero is not allowed."
                    break
                result /= operand[i]
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
    # cherrypy.config.update({'server.socket_host': ''})
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()
    cherrypy.engine.block()