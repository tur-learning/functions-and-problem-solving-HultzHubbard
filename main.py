# Calculating the number of chocolate bars required to maintain a metabolism based off of the Basal Metabolic Rate

def BMR():
    print("We will calculate the number of chocolate bars required to maintain a metabolism based off the Basal Metabolic Rate for both a man and a woman.\n")
    # User inputs
    weight = int(input("Enter weight of individual (kg): "))
    hight = int(input("Enter hight of individual (cm): "))
    age = int(input("Enter age of individual (years): "))

    # Calculations
    totalBMRmen = (weight * 13.7516) + (hight * 5.0033) - (age * 6.755) + 66.473
    totalBMRwomen = (weight * 9.5634) + (hight * 1.8496) - (age * 4.6756) + 655.0955

    # Final print statements
    print("\nNumber of chocolate bars required for men's metabolism: ", + (totalBMRmen / 214))
    print("Number of chocolate bars required for women's metabolism: ", + (totalBMRwomen / 214))

BMR()

# ------------------------------------------------------------------------------------------------------------------------------------
# Converting Celsius to Fahrenheit

def temp():
    print("\nWe will convert Celsius to Fahrenheit\n")
    # User input
    celcius = int(input("Enter temperature in Celcius: "))

    # Calculations
    temp = int((celcius * (9/5)) + 32)

    # Final print statement
    print("The temperature coverted to Fahrenheit is: " + str(temp) + " degrees.")

temp()

# -------------------------------------------------------------------------------------------------------------------------------------------
# Converting number of seconds into hours, minutes, and seconds

def time():
    print("\nWe will divide seconds into hours, minutes, and seconds.\n")
    # User input
    RawSeconds = int(input("Please enter the number of seconds you wish to be divided into hours, minutes, and seconds: "))

    # Calculations
    hours = int(RawSeconds / 3600)
    minutes = int(((RawSeconds / 3600) % 1) * 60)
    seconds = int(((((RawSeconds / 3600) % 1) * 60) % 1) * 60)

    print(f"{RawSeconds} seconds is {hours} hours, {minutes} minutes, and {seconds} seconds.")

time()
