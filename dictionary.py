import json
from difflib import get_close_matches


data = json.load(open("data.json"))


def define(w):
    w = w.lower()
    close_match = get_close_matches(w, data.keys())
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(close_match) > 0:
        print("Did you mean %s?" % close_match[0])
        yn = input("Enter Y (Yes) or N (No): ")
        if yn == "Y" or yn == "y":
            return data[close_match[0]]
        elif yn == "N" or yn == "n":
            return "That word doesn't exist. Please try again."
        else:
            return "Sorry, we didn't understand your entry. Please try again."
    else:
        return "That word does not exist. Please try again."


word = input("Enter a word: ")

output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

