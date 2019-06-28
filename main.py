from iss import iss_crew, iss_location, iss_pass_times
def main():
    issApiUrl = "http://api.open-notify.org/"

    iss_crew(issApiUrl)
    iss_location(issApiUrl)
    iss_pass_times(issApiUrl)



if __name__ == "__main__":
    main()