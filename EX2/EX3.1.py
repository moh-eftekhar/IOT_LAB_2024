import cherrypy
import json
import requests

responce = requests.get("https://catalog-p4iot.onrender.com/")
if responce.status_code == 200:
    responce_json = responce.json()
    print ( json.dumps(responce_json, indent=4))

# def string_reverse(string):
#     return string[::-1]
# class HelloWorld:
#     exposed = True
#     def GET(self,*uri,**params):
#         output = ""
#         if len(uri) > 0:
#             for pathi in uri:
#                 output += string_reverse(pathi) + "<br>"
            

        
#         # if params != {}:
#         #     output += "<br>params: " + ','.join(params)
        
#         return output
    
#     def PUT(self, *uri, **params):
#         # bodyRaw = "body postman"
#         bodyRaw = cherrypy.request.body.read()
#         bodyRawJ = json.loads(bodyRaw)
#         for key in bodyRawJ:
#             bodyRawJ[key] = string_reverse(bodyRawJ[key])

#         return json.dumps(bodyRawJ)

    
# if __name__ == '__main__':
#     conf = {
#         '/': {
#             'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
#             'tools.sessions.on': True
#         }
#     }

#     webService = HelloWorld()
#     cherrypy.tree.mount(webService, '/', conf)
#     cherrypy.config.update({'server.socket_host': '0,0,0,0'})
#     cherrypy.config.update({'server.socket_port': 8080})
#     cherrypy.engine.start()
#     cherrypy.engine.block()
