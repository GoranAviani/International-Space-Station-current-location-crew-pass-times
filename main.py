from iss import iss_crew, iss_location, iss_pass_times
def main():


    iss_crew()
    iss_location()




    userInput = input("How many future pass time would you like to see? Choose between 1 and 5:\n")
    if userInput.isnumeric():
        userInput = int(userInput)
        if userInput > 0 and userInput < 6:
            iss_pass_times(userInput)
        else:
            print("Please choose a number from 1 to 5.")
    else:
        print("Please type numbers only.")





if __name__ == "__main__":
    main()