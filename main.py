#!/usr/bin/python3

from pprint import pprint

import database
import format
from config import COMMIT_BEFORE_EXIT, EXIT_WHEN_EXCEPTION
from shortcuts import *

database.init()


HELP = '''
dua username        Output user's accepted submissions into 'outputs/{username}.csv' in SYZOJ style
                    Only keep the oldest submission for the same problem
duaa                Run `dua {user}` for all users in the database
exec command        Run `exec(command)` in Python
exit                Exit the program
help                Show the help text
query [params]      Query in the database and print the results
ua username         Crawl user's accepted submissions from the site and store them into the database
uaa                 Run `ua {user}` for all users in the database
users               Print all users in the database
'''.strip()

# update [params]     Crawl specified submissions from the site and store them into the database


print('''
Libuer version 0.1a 2020-07-19 11:14:07

'''.strip())

command = ''
while True:
    if not command:
        s = input('libuer> ')
    else:
        s = input('   ...> ')

    if s and s[-1] == '\\':
        command += s[:-1]
        continue

    command += s
    command = command.strip()

    try:
        if command.find(' ') != -1:
            params = command[command.find(' '):].strip()
        else:
            params = ''

        if command.find('dua') == 0:
            dumpuserac(params)
        elif command.find('duaa') == 0:
            dumpalluserac()
        elif command.find('exec') == 0:
            exec(command)
        elif command.find('exit') == 0:
            if COMMIT_BEFORE_EXIT:
                database.commit()
            print('# Have a nice day')
            exit(0)
        elif command.find('help') == 0:
            print(HELP)
        elif command.find('query') == 0:
            print(query(params))
        elif command.find('ua') == 0:
            upuserac(params)
        elif command.find('uaa') == 0:
            upalluserac()
        elif command.find('users') == 0:
            print(' '.join(sorted(queryusers())))
        else:
            print('! Unknown command')
        
    except Exception as e:
        if EXIT_WHEN_EXCEPTION:
            raise e
        else:
            print('!', type(e), e.args[0])
    command = ''
