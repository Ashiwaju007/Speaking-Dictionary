import json
from difflib import get_close_matches
import pyttsx3

engine= pyttsx3.init()
engine.setProperty('rate', 125)

#load JSON data
data = json.load(open("data.json"))



#function to return meaning of the word from data
def getMeaning(w):
    #for case sensitivity
    w = w.lower()
    #if-else to check word exist in our data or not
    if w in data:
        return data[w]
    #give matching word
    elif len(get_close_matches(w,data.keys())) > 0:
        close_match = get_close_matches(w,data.keys())[0]
        print("Did you mean %s instead? Enter Y if yes or N if no: " % close_match)
        choice = input()
        choice = choice.lower()
        if choice == 'y':
            return data[close_match]
        elif choice == 'n':
            print ("\nThe word doesn't exist. Please double check it.")
            engine.say("The word doesn't exist. Please double check it.")
            engine.runAndWait()
            engine.stop()
        else:
            print("\nSorry, unfortunately we didn't understand your word.")
            engine.say("Sorry, unfortunately we didn't understand your word.")
            engine.runAndWait()
            engine.stop()
    else:
        print("\nThe word doesn't exist. Please double check it.")
        engine.say("The word doesn't exist. Please double check it.")
        engine.runAndWait()
        engine.stop()

c = 'y'
while c == 'y':

    # take word from user
    word = input('Enter word: ')

    #function call to get meaning of the word entered by user
    meaning = getMeaning(word)
    meaning_string = ""
    #printing meaning of the word in console
    if type(meaning) == list:
        for item in meaning:
            meaning_string += item
            print(meaning_string)
            engine.say(meaning_string)
            engine.runAndWait()
            engine.stop()
            print("Don you wish to search another word? Y or N")
            c=input().lower()
    else:
        c = "N"