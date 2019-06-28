import requests
import datetime

def get_result_from_iss(fullApiUrl):
    pass

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


def iss_location(issApiUrl):
    issLocationUrl = "iss-now.json"
    result = requests.get(issApiUrl + issLocationUrl)
    if result.status_code == 200:
        message = result.json()
        dateAndTime = datetime.datetime.fromtimestamp(message["timestamp"])

        issCoordinates = message['iss_position']

        print("\nAnja, we have made a request for ISS location at {}." .format(dateAndTime))


        print("\nCurrent location coordinate of the space station are latitude: {}, longitude: {}."
              .format(issCoordinates['latitude'], issCoordinates['longitude']))

    elif result.status_code == 404:
        print("The page is not reachable")
    else:
        print("Something has good wrong.")


