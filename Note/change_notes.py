from note import Note
import os.path
import os
import read_notes


def change_note(file):
    note = read_notes.load_json(file)
    if note:
        print("Что вы хотите изменить: ")
        change = input("name/text ")

        if change.lower() == "name":
            print("Имя заметки будет изменено")
            name = input("Введите новое имя для заметки: ")
            note.change_name(name)
            del_note(file)
            print(f"Файл {note.get_file_name()} создан")
        elif change.lower() == "text":
            note.text = input("Введите новую заметку: ")

        note.save_json()


def del_note(file):
    if os.path.exists(file):
        os.remove(file)
        print(f"Файл {file} удален")
    else:
        print(f"Файл {file} не найден")
