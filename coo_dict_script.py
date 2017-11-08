import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]

    elif w.title() in data:
        return data[w.title()]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("You mean %s? (Y/N)" %get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n":
            return "No such word, yo!"
        else:
            return "No comprende.."
    else:
        return "I don't know that word. So..."

word = input("What's the word foo' ? ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
