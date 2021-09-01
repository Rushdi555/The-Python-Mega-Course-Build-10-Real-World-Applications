import json
from difflib import get_close_matches

data = json.load(open('data.json'))


def translate(keyword): 
    lower_key = keyword.lower()
    if lower_key in data:
        return data[lower_key]
    elif len(get_close_matches(lower_key, data.keys(), cutoff=0.6)) > 0:
        closest = get_close_matches(lower_key, data.keys())[0]
        cor = input('Did you mean %s? (Y/N)'  %  closest)
        if cor == 'Y':
            return data[closest]
        else:
            return 'error'
    else:
        return 'error'



def start():
    stop = True
    while stop:
        word = input('Enter word: ')
        output = translate(word)
        if type(output) == list:
            for item in output:
                print(item)
            stop = False
        elif output == 'error':
            print('word not found please try again')
        else:
            print(output)
            stop = False

start()

        
#done

