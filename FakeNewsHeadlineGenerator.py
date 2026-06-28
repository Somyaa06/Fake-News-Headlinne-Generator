# import the random module

import random
 #1- create subjects

subjects=[
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys",
    "Prime Minister Modi",
    "Auto Rickshaw Driver from Delhi"
    ]

actions=[
    "Launches",
    "Cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates"
]

places_or_things=[
    " at Red Fort",
    "in Mumbai Local Train ",
    " a plate of samosa",
    "inside parliament ",
    " at Ganga Ghat",
    " during IPL Match",
    "at India Gate ",
]

#3- Start the headline generation loop

while True:
    subject=random.choice(subjects)
    action=random.choice(actions)
    place_or_thing=random.choice(places_or_things)

    headline=f" BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input=input("\nDo you want another headline? (Yes/No).strip()")
    if user_input=="No":
        break

# print goodbye message
print("\n Thanks for using the Fake News Headline Generator. Have a fun day")