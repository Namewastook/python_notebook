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

while True:
    content = input("What is the note? \n>")
    note_id = counter
    note = (note_id, str(now), content)
    notebook.append(note)
    counter += 1
    print(notebook)
