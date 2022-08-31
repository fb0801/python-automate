import sys
import clipboard
import json

#clipboard.copy("abc")

def save_items(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

save_items("test.json", {"key": "value"})

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

