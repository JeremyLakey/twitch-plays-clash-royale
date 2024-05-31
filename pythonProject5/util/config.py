import requests
import json

conf_file = open("./conf/config.json")
conf = json.load(conf_file)

def getConfig(s):
    global conf
    return conf[s]

