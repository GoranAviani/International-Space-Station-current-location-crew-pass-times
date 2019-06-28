import requests

def iss_crew(issApiUrl):
    issCrewUrl = "astros.json"
    result = requests.get(issApiUrl + issCrewUrl)
    if result.status_code == 200:
        message = result.json()
        print("\nAnja, there are " + str(message['number']) + " cosmonauts in space right now.")
        print("-------------------------------------------------- \nAnd ther are: \n")
        for x in message['people']:
            print("* {} is in space craft {}. \n" .format(x['name'], x['craft']))
    elif result.status_code == 404:
        print("The page is not reachable")
    else:
        print("Something has good wrong.")


