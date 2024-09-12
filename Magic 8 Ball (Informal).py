import random

print("==============================")
title = "magic 8 ball".upper()
print(title.center(30, "="))
print("==============================")

input("Press enter to begin!")
playing = input('Think really hard for what you want to get a prediction for...\nReady for a prediction? (y/n): ').lower().strip()

while playing not in ['y', 'n']:
    print("Invalid input. Please enter 'y' for yes or 'n' for no.")
    print(".................................")
    playing = input("Do you want a prediction? (y/n): ").lower().strip()
    print(".................................")

predictions = [
    "Hell yeah!✌️",
    "Definitely!💯",
    'No doubt!👍',
    'Yes, absolutely.😊',
    'You bet!🙌',
    'Yep, sure does!👌',
    'Probably 😒',
    'Looks good 😎',
    'Yep 😏',
    'Seems like it 🧐',
    'Try again later, I guess 😐',
    'Not telling you now 🥱',
    'Ask me later 😑',
    "Can't say right now 🤫",
    'Ask again later 😴',
    "Nope, don't count on it 🙂‍↔️",
    'Looks bad 😧',
    'Nah, not happening 😪',
    'Doubt it 😓',
    'Nope 👎'
]

while True:
    if playing == 'y':
        print("Prediction-->", random.choice(predictions))
        print(".................................")
        while True:
            playing = input('Do you want another prediction? (y/n): ').lower().strip()
            print(".................................")
            if playing == 'y':
                break
            elif playing == 'n':
                print("Thanks for playing!")
                exit()
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
                print(".................................")
    else:
        print("Thanks for playing!")
        print(".................................")
        exit()
