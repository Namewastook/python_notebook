from datetime import date
"""
Notebook app

A note has 3 parts:
1. ID
2. Content
3. Date/time
"""


counter = 1
notebook = []
now = date.today()

user_response = input("Would you like to make a note? \n"
                      "1. Add a note\n"
                      "2. Print a note \n"
                      "3. Exit\n>"
                      )

if user_response == "1":
    content = input("What is the note? \n>")
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1
elif user_response == "2":
    for note in notebook:
        print(f"Id: {note[0]}|{note[2]}")
elif user_response == "3":
    exit()
else:
    print(notebook)
