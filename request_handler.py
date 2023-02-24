import requests

def sendRequest(url, path):
  response = requests.get(url + path)
  if response.status_code == 200:
    return response
  else
    return false
