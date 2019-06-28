from iss import iss_crew, iss_location
def main():
    issApiUrl = "http://api.open-notify.org/"

    iss_crew(issApiUrl)
    iss_location(issApiUrl)


if __name__ == "__main__":
    main()