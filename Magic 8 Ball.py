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
    "It is certain.",
    "It is decidedly so.",
    'Without a doubt.',
    'Yes - definitely.',
    'You may rely on it.',
    'As I see it, yes.',
    'Most likely.',
    'Outlook good.',
    'Yes.',
    'Signs point to yes.',
    'Reply hazy, try again.',
    'Better not tell you now.',
    'Ask again later.',
    'Cannot predict now.',
    'Concentrate and ask again.',
    "Don't count on it.",
    'Outlook not so good.',
    'My sources say no.',
    'Very doubtful.',
    'No.'
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
