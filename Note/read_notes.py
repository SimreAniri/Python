import os
import os.path
from note import Note


def read_dir(my_dir=""):
    list_file = []
    for f in os.listdir():
        if os.path.isfile(f) and f.endswith(".json"):
            list_file.append(my_dir + f)

    return list_file


def read_jsons_to_list(list_file):
    list_note = []
    for f in list_file:
        list_note.append(load_json(f))
    return list_note


def read_note(file):
    note = load_json(file)
    if note:
        print(note.print_note())


def load_json(file):
    note = Note()
    if note.read_json(file):
        return note
    return None
