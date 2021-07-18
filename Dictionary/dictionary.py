import json
from difflib import get_close_matches

data = json.load(open("data.json"))
print()


def find_definition(word):
    if word.lower() in data:
        print_definitions(word, data[word.lower()])
    elif word.upper() in data:
        print_definitions(word, data[word.upper()])
    elif word.title() in data:
        print_definitions(word, data[word.title()])
    else:
        closer_matches = get_close_matches(word, data.keys(), cutoff=0.8)
        if len(closer_matches) > 0:
            user_response = input(
                "Did you meant \"%s\", Yes(y) or No(any key): " % closer_matches[0])
            if(user_response == 'y'):
                print_definitions(closer_matches[0], data[closer_matches[0]])
            else:
                print()
        else:
            print("Sorry, the word you enter doesn't exist. Please double check it\n")


def print_definitions(word, definitions):
    print("\n%s:" % word.title())
    for definition in definitions:
        print(" * " + definition)
    print()


try:
    word_to_search = ""
    while word_to_search != "e":
        word_to_search = input(
            "Enter the world you want to know its meaning, enter (e) to exit : ").strip()
        if word_to_search != 'e':
            find_definition(word_to_search)
    print("\nThanks for coming\n")
except KeyboardInterrupt:
    print("\n\nThanks for coming\n")
