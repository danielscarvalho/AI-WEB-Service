import requests

def soma(a, b):
    return float(a) + float(b)

def ddg(query):
    DDG_URL=f"https://api.duckduckgo.com/?q={query}&format=json"
    result=[]
    ddg_json = requests.get(DDG_URL).json()
    result.append(ddg_json["Abstract"])
    for rt in ddg_json["RelatedTopics"]:
       result.append(rt["Text"])
    return result 

