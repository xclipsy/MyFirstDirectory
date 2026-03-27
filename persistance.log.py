"""
The script handles the persistence of a user's daily blocker by saving it to a local text file. 
Depending on the user's input, it will either safely append the new entry or intentionally 
overwrite the entire database after a confirmation warning. Later, the program can fetch 
the stored blockers to display them, allowing the user to review their documented issues before 
they reach out to their team for help.
"""

import os

Daily_Blocker = []

ask_the_blocker = input('What is your Daily Blocker? ')
Daily_Blocker.append(ask_the_blocker)

# Correctly checks if the file exists and has a size greater than 0
file_empty = not (os.path.exists('database.txt') and os.path.getsize('database.txt') > 0)

choice = input('Do you want to append (a) or overwrite (w) (a/w): ').lower()
if choice == 'w':
    warning = input('WARNING! Really you wanna overwrite the database, all the content will be erased (y/n): ').lower()
    if warning == 'y':
        with open("database.txt", 'w') as file:
            file.write(ask_the_blocker)
else:
    print('Default route, APPEND')
    with open("database.txt", 'a') as file:
        file.write('\n' + ask_the_blocker)

def fetch_blocker():
    # Now this correctly evaluates if the file has data to read
    if not file_empty:
        with open("database.txt", 'r') as file:
            for i in file:
                print(i.strip())
    else:
        print('There are no blockers found.')
