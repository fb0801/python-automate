import sys
import clipboard
import json

#clipboard.copy("abc")

#save items
def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

#load items
def load_items(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
        return data

if len(sys.argv) == 2:
    command =sys.argv[1]
    print (command)

    if command == "save":
        print('save')
    elif command == 'load':
        print ('load')
    else:
        print('unknown command')
else:
    print("please pass exactly one command")

