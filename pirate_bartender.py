questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

responses = {}

def order():
    """I ask the user the questions"""
    for key,val in questions.items():
        responses[key] = input("{}".format(val))
        if responses[key] == "y":
            responses[key] = True
        elif responses[key] == "yes":
            responses[key] = True
        else:
            responses[key] = False

import random

def recipe():
    drink = []
    for key,val in responses.items():
        if responses[key] == True:
            drink.append(random.choice(ingredients[key]))
        else:
            pass
    print(drink)

if __name__ == '__main__':
    order()
    recipe()