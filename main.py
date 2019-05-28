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


def menu():
    user_response = input("Would you like to make a note? \n"
                          "1. Add a note\n"
                          "2. Print a note \n"
                          "3. Exit\n>"
                          )
    return user_response


def note_create():
    content = input("What is the note? \n>")
    global counter
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1


def print_notes():
    for note in notebook:
        print(f"Id: {note[0]}|{note[2]}")


def run():
    while True:
        choice = menu()
        if choice == "1":
            note_create()
        elif choice == "2":
            print_notes()
        elif choice == "3":
            exit()
        else:
            print(notebook)


if __name__ == "__main__":
    run()
