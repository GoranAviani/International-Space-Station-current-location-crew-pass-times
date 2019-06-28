import requests

def iss_crew(issApiUrl):
    issCrewUrl = "astros.json"
    result = requests.get(issApiUrl + issCrewUrl)
    if result.status_code == 200:
        message = result.json()
        print("Anja, there are " + str(message['number']) + " cosmonauts in space right now.")
        
    else:
        print("Something has good wrong.")


