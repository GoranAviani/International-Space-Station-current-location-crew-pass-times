from iss import iss_crew, iss_location, iss_pass_times
def main():
    issApiUrl = "http://api.open-notify.org/"

    iss_crew(issApiUrl)
    iss_location(issApiUrl)




    userInput = input("How many future pass time would you like to see? Choose between 1 and 5:\n")
    if userInput.isnumeric():
        userInput = int(userInput)
        if userInput > 0 and userInput < 6:
            numOfTimesIssPassesOver = userInput
        else:
            print("Please choose a number from 1 to 5.")
    else:
        print("Please type numbers only.")

    iss_pass_times(issApiUrl, numOfTimesIssPassesOver)



if __name__ == "__main__":
    main()