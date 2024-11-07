import cherrypy
import json
import requests

responce = requests.get("https://catalog-p4iot.onrender.com/")
r = responce.json()
print(r)