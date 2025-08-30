print(" __      __          _ _ _    _          ")
print(" \ \    / /__ _ _ __| | (_)__| |_        ")
print("  \ \/\/ / _ \ '_/ _` | | (_-<  _|       ")
print("   \_/\_/\___/_| \__,_|_|_/__/\__|       ")
print("  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ ")
print(" | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|")
print("  \___\___|_||_\___|_| \__,_|\__\___/_|         > Developed by: github.com/andrelfmp3")
print("")                                     
print("IMPORTANT: If you don’t know how to answer, just press ENTER")
print("If the answer is yes, type Y or press ENTER")
print("Always use numbers in numeric form (ex: 11, not eleven)")

# functions ----------------------------------------

wordlistCounter = 0
wordlistItems = []

def counter_input(prompt):
    global wordlistCounter
    answer = input(prompt)
    if answer != "":
        wordlistCounter += 1
    return answer

def save_to_wordlist(value, file):
    if value not in [None, ""]:
        file.write((value) + "\n")
        wordlistItems.append(value)
        
def letter_to_number(word):
    substitutions = {
        'a': '4', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '5', 'S': '5',
    }
    result = ""
    for char in word:
        if char in substitutions:
            result += substitutions[char]
        else:
            result += char
    return result


# data ----------------------------------------

name = counter_input("Name: ")
nickname = counter_input("Nickname: ")
mainNick = counter_input("Main Nick (@): ")
birthYear = counter_input("Birth year (number): ")
birthMonth = counter_input("Birth month (number): ")
birthDay = counter_input("Birth day (number): ")
fatherName = counter_input("Father's name: ")
motherName = counter_input("Mother's name: ")
workplace = counter_input("Workplace: ")
cityBorn = counter_input("City of birth: ")
cityNow = counter_input("Current city: ")
jobTitle = counter_input("Job title: ")

spouse = {}
if input("Do you have a spouse? (Y/n) ").lower() in ["y", ""]:
    spouse["name"] = counter_input("Spouse's name: ")
    spouse["nickname"] = counter_input("Spouse's nickname: ")
    spouse["nick"] = counter_input("Spouse's main nick (@): ")
    spouse["birthYear"] = counter_input("Spouse's birth year: ")
    spouse["birthMonth"] = counter_input("Spouse's birth month: ")
    spouse["birthDay"] = counter_input("Spouse's birth day: ")
    spouse["workplace"] = counter_input("Spouse's workplace: ")
    spouse["jobTitle"] = counter_input("Spouse's job title: ")
    spouse["startYear"] = counter_input("Year you started dating: ")
    spouse["startMonth"] = counter_input("Month you started dating: ")
    spouse["startDay"] = counter_input("Day you started dating: ")

marriage = {}
if input("Are you married? (Y/n) ").lower() in ["y", ""]:
    marriage["name"] = counter_input("Name: ")
    marriage["nickname"] = counter_input("Nickname: ")
    marriage["nick"] = counter_input("Main Nick (@): ")
    marriage["birthYear"] = counter_input("Birth year (number): ")
    marriage["birthMonth"] = counter_input("Birth month (number): ")
    marriage["birthDay"] = counter_input("Birth day (number): ")
    marriage["fatherName"] = counter_input("Father's name: ")
    marriage["motherName"] = counter_input("Mother's name: ")
    marriage["workplace"] = counter_input("Workplace: ")
    marriage["cityBorn"] = counter_input("City of birth: ")
    marriage["cityNow"] = counter_input("Current city: ")
    marriage["jobTitle"] = counter_input("Job title: ")

children = []
if input("Do you have children? (y/N) ").lower() in ["y"]:
    count = int(counter_input("Number of children: "))
    for i in range(count):
        child = {}
        child["name"] = counter_input(f"Name of child {i+1}: ")
        child["nick"] = counter_input(f"Main nick (@) of child {i+1}: ")
        child["birthYear"] = counter_input(f"Birth year of child {i+1}: ")
        child["birthMonth"] = counter_input(f"Birth month of child {i+1}: ")
        child["birthDay"] = counter_input(f"Birth day of child {i+1}: ")
        child["nickname"] = counter_input(f"Nickname of child {i+1}: ")
        children.append(child)

pets = []
if input("Did you have any pets? (y/N) ").lower() in ["y"]:
    count = int(counter_input("Number of pets: "))
    for i in range(count):
        pet = {}
        pet["name"] = counter_input(f"Name of pet {i+1}: ")
        pet["birthYear"] = counter_input(f"Birth year of pet {i+1}: ")
        pet["birthMonth"] = counter_input(f"Birth month of pet {i+1}: ")
        pet["birthDay"] = counter_input(f"Birth day of pet {i+1}: ")
        pet["species"] = counter_input(f"Species of pet {i+1}: ")
        pet["breed"] = counter_input(f"Breed of pet {i+1}: ")
        pets.append(pet)

cars = []
if input("Did you have any cars? (y/N) ").lower() in ["y"]:
    count = int(counter_input("Number of cars: "))
    for i in range(count):
        car = {}
        car["plate"] = counter_input(f"License plate of car {i+1}: ")
        cars.append(car)

extraWords = []
update = 1
print("Other relevant words: (Press Enter to exit)")
while True:
    word = input(f"Word {update}: ")
    if word == "":
        break
    extraWords.append(word)
    wordlistCounter += 1
    update += 1

# additional combinations --------------------------------
print(f"\nNumber of registered words: {wordlistCounter}")

concat = input("More combinations: Concatenate registered numbers at the end of words? Ex: word + 123, word123 (Y/n)").lower()
if concat in ["y", ""]:
    concat = True
toNumber = input("More combinations: Replace letters with numbers? Ex: A -> 4, E -> 3, (Y/n) ").lower()
if toNumber in ["y", ""]:
    toNumber = True

# wordlist ----------------------------------------
with open("wordlist.txt", "w", encoding="utf-8") as file:
    # Personal data
    save_to_wordlist(name, file)
    save_to_wordlist(nickname, file)
    save_to_wordlist(mainNick, file)
    save_to_wordlist(birthYear, file)
    save_to_wordlist(birthMonth, file)
    save_to_wordlist(birthDay, file)
    save_to_wordlist(fatherName, file)
    save_to_wordlist(motherName, file)
    save_to_wordlist(workplace, file)
    save_to_wordlist(cityBorn, file)
    save_to_wordlist(cityNow, file)
    save_to_wordlist(jobTitle, file)

    # Spouse
    for value in spouse.values():
        save_to_wordlist(value, file)

    # Marriage
    for value in marriage.values():
        save_to_wordlist(value, file)

    # Children
    for child in children:
        for value in child.values():
            save_to_wordlist(value, file)

    # Pets
    for pet in pets:
        for value in pet.values():
            save_to_wordlist(value, file)

    # Cars
    for car in cars:
        for value in car.values():
            save_to_wordlist(value, file)

    # Extra words
    for word in extraWords:
        save_to_wordlist(word, file)

    if concat:
        numbersInWordlist = []
        for item in wordlistItems:
            if item.isnumeric():
                numbersInWordlist.append(item)
        for word in wordlistItems:
            if not word.isnumeric():
                for number in numbersInWordlist:
                    combo = word + number
                    save_to_wordlist(combo, file)

    if toNumber:
        for word in wordlistItems:
            save_to_wordlist(letter_to_number(word), file)