from datetime import date
"""
Notebook app

A note has 3 parts:
1. ID
2. Content
3. Date/time
"""

notebook = []

counter = 1
note_id = counter

counter += 1

now = date.today()

content = "this is content"

note = (note_id, str(now), content)

notebook.append(note)

print(notebook)
