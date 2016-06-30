import random

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

adjectives = ["Fluffy ", "Salty "]
nouns = ["Chincilla", "Sea-Dog"]

drinknames = {}

customers = {}

def order():
    responses = {}
    for key,val in questions.items():
        print(val)
        responses[key] = input().lower()
        if responses[key] == "y":
            responses[key] = True
        elif responses[key] == "yes":
            responses[key] = True
        else:
            responses[key] = False
        print("")
    return responses

def recipe(responses):
    drink = []
    for key,val in responses.items():
        if responses[key] == True:
            drink.append(random.choice(ingredients[key]))
        else:
            continue
    return drink
    
def namedrink():
    for key,val in customers.items():
        drinknames[key] = random.choice(adjectives) + random.choice(nouns)
        customers[key] = drinknames[key]

def introduction():
    print("What's yer name?")
    name = input()
    customers[name] = "placeholder"

def main():
    introduction()
    drinking = True
    while drinking:
        for key,val in customers.items():
            if customers[key] == "placeholder":
                responses = order()
                drink = recipe(responses)
                print("One drink coming up.")
                print("It's full of good stuff. The recipe is: {}".format(drink))
                namedrink()
                print("I call it a {}".format(drinknames[key]))
                print("")
            else:
                print("Here's another {}, {}!".format(customers[key],key))
        print("Want another round?")
        print("")
        another = input().lower()
        if another == "y":
            continue
        elif another == "yes":
            continue
        else:
            print("I think you've had enough anyway...")
            break
    
if __name__ == "__main__":
    main()