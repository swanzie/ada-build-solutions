#madlib assignment
#accepts input from the user and outputs a completed MadLib
#at least 10 different parts of speech to fill in madlib

my_madlib = {}

print("Welcome to my MadLib program. Please enter some information below:\n")

#asking user for inputs
my_madlib = {
    "animal1": input("animal: "),
    "name1": input("name: "),
    "gerund": input("verb ending in 'ing': "),
    "hobby": input("hobby: "),
    "noun1": input("noun: "),
    "name2": input("name: "),
    "number": input("integer number: "),
    "noun2": input("noun: "),
    "city": input("city: "),
    "landscape": input("noun: "),
    "landscape_adj": input("adjective: "),
    "color": input("color: "),
    "activity": input("verb: "),
    "location": input("place to be: "),
    "food": input("food: "),
    "drink": input("drink: ")
}

#printing madlib using user inputs
print(f"\nOnce upon a time there was an {my_madlib['animal1']} named {my_madlib['name1'].capitalize()}.")
print(f"{my_madlib['name1'].capitalize()} loved {my_madlib['gerund']} and {my_madlib['hobby']}.")
print(f"{my_madlib['name1'].capitalize()} had a best friend who was a {my_madlib['noun1']} named {my_madlib['name2'].capitalize()}.")
print(f"{my_madlib['name2'].capitalize()} had {my_madlib['number']} {my_madlib['noun2']}s.")
print(f"{my_madlib['name1'].capitalize()} and {my_madlib['name2'].capitalize()} lived in {my_madlib['city'].capitalize()} near the {my_madlib['landscape']}.")
print(f"The {my_madlib['landscape']} was {my_madlib['landscape_adj']} and {my_madlib['color']}.")
print(f"One of their favorite things to do was to {my_madlib['activity']} in {my_madlib['location']} and eat {my_madlib['food']} and drink {my_madlib['drink']}.") 