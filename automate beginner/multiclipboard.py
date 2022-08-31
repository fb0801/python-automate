import sys
import clipboard
import json

#clipboard.copy("abc")

if len(sys.argv) == 2:
    command =sys.argv[1]
    print (command)

    if command == "save":
        print('save')
    elif command == 'load':
        print ('load')
    else:
        print('unknown command')
    
