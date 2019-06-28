import requests
import datetime

def get_result_from_iss(fullApiUrl):
    result = requests.get(fullApiUrl)
    if result.status_code == 200:
        message = result.json()
        return message
    elif result.status_code == 404:
        print("The page is not reachable")
    else:
        print("Something has good wrong.")

def iss_crew(issApiUrl):
    issCrewUrl = "astros.json"
    message = get_result_from_iss(issApiUrl + issCrewUrl)
    print("\nAnja, there are " + str(message['number']) + " cosmonauts in space right now.")
    print("-------------------------------------------------- \nAnd ther are: \n")
    for x in message['people']:
        print("* {} is in space craft {}. \n" .format(x['name'], x['craft']))

def iss_location(issApiUrl):
    issLocationUrl = "iss-now.json"
    message = get_result_from_iss(issApiUrl + issLocationUrl)
    dateAndTime = datetime.datetime.fromtimestamp(message["timestamp"])
    issCoordinates = message['iss_position']
    print("\nAnja, we have made a request for ISS location at {}." .format(dateAndTime))
    print("\nCurrent location coordinate of the space station are latitude: {}, longitude: {}."
          .format(issCoordinates['latitude'], issCoordinates['longitude']))


def iss_pass_times(issApiUrl):
    #http://api.open-notify.org/iss-pass.json?lat=-39.0067&lon=-43.5363&alt=10&n=1
    #lat The latitude of the place to predict passes -80..80 	degrees 	required
    #lon The longitude of the place to predict passes -180..180 	degrees required
    #alt The altitude of the place to predict passes 0..10,000 	meters
    #n The number of passes to return 1..100
    pass

    message = get_result_from_iss(issApiUrl + issCrewUrl)
