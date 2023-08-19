from note import Note


def add_note():
    name = input("Введите название заметки: ")
    text = input("Введите текст заметки: ")
    note = Note(name, text)
    if note.save_json():
        print(f"Заметка {note.get_file_name()} успешно создана")
