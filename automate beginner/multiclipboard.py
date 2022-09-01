import sys
import clipboard
import json

#application to copy item

SAVED_DATA = "clipboard.json"



#save items
def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

#load items
def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data

if len(sys.argv) == 2:
    command =sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input('Enter a key: ')
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
    elif command == 'load':
        print ('load')
    else:
        print('unknown command')
else:
    print("please pass exactly one command")

