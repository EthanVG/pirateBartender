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

def ask():
    response = {}

    for k, v in questions.items():
        i = input(v + " ")
        if (i == "y") or (i == "yes"):
            response[k] = True
        else:
            response[k] = False
    construct(response)
    
def construct(response):
    drink = list()
    
    for k, v in response.items():
        if v == True:
            drink.append(random.choice(ingredients[k]))
    print(drink)
    
    output = "Arr, here's yer drink with a"
    
    for i in drink:
        if (i == drink[-1]):    #Last item
            connect = ", and a "
        elif (i == drink[0]):   #First item
            connect = " "
        else:                   #Middle
            connect = ", a "
        output = output + connect + i
    output += "." 
            
    print(output)
        
            
    
    
    
if __name__ == '__main__':
    ask()
        