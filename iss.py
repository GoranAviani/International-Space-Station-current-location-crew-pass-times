import requests
import datetime

def user_location():
    message = get_result_from_requests("user_location", "http://ip-api.com/json")
    lon = message['lon']
    lat = message['lat']
    return lat, lon

def get_result_from_requests(callingFunction = None, params = None):
    issApiUrl = "http://api.open-notify.org/"

    urlEndpoint = ""
    if callingFunction == "iss_crew":
        urlEndpoint = "astros.json"
    elif(callingFunction == "iss_location"):
        urlEndpoint = "iss-now.json"
    elif(callingFunction == "iss_pass_times"):
        urlEndpoint = "iss-pass.json"
    elif (callingFunction == "user_location"):
        issApiUrl = params
    else:
        print("*** There is a unknown function making a request ***")

    issApiUrl = issApiUrl + urlEndpoint

    if params == None:
        result = requests.get(issApiUrl)
    else:
        result = requests.get(issApiUrl, params)
    if result.status_code == 200:
        message = result.json()
        return message
    elif result.status_code == 404:
        print("The page is not reachable")
    else:
        print("Something has gone wrong.")

def iss_crew():
    message = get_result_from_requests("iss_crew")
    print("\nAnja, there are " + str(message['number']) + " cosmonauts in space right now.")
    print("-------------------------------------------------- \nAnd ther are: \n")
    for x in message['people']:
        print("* {} is in space craft {}. \n" .format(x['name'], x['craft']))

def iss_location():
    message = get_result_from_requests("iss_location")
    dateAndTime = datetime.datetime.fromtimestamp(message["timestamp"])
    issCoordinates = message['iss_position']
    print("\nAnja, we have made a request for ISS location at {}." .format(dateAndTime))
    print("\nCurrent location coordinate of the space station are latitude: {}, longitude: {}."
          .format(issCoordinates['latitude'], issCoordinates['longitude']))


def iss_pass_times(numOfTimesIssPassesOver):
    #http://api.open-notify.org/iss-pass.json?lat=-39.0067&lon=-43.5363&alt=10&n=1
    #lat The latitude of the place to predict passes -80..80 	degrees 	required
    #lon The longitude of the place to predict passes -180..180 	degrees required
    #alt The altitude of the place to predict passes 0..10,000 	meters
    #n The number of passes to return 1..100

    # payload = {'key1': 'value1', 'key2': 'value2'}
    # r = requests.get('https://httpbin.org/get', params=payload)

    userLat, userLon = user_location()
    print(userLat)
    print(userLon)
    userAlt = "10"
    requestData = {'lat' : userLat, 'lon' : userLon, 'alt' : userAlt, 'n' : numOfTimesIssPassesOver}
    message = get_result_from_requests("iss_pass_times", requestData)

    for x in message['response']:
        seconds = x['duration']
        time = datetime.datetime.fromtimestamp(x['risetime'])
        print("Anja the ISS will be visible for {} seconds on {}" .format(seconds, time))