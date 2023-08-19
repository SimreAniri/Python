import read_notes
from datetime import datetime, date


def find_notes_by_date(my_date):
    notes_by_date = []
    my_date = [int(i) for i in my_date.split("-")]
    my_date = date(*my_date)
    note_list = read_notes.read_jsons_to_list(read_notes.read_dir())

    for note in note_list:
        note_date = note.get_data()
        if my_date == note_date.date():
            notes_by_date.append(note.get_file_name())

    return notes_by_date
