from note import Note
import read_notes
import change_notes
from add_note import add_note
import os


path = os.getcwd()
print("Добро пожаловать в менеджер заметок")
print("Для управления используйте следующие команды:\n"
      "add - добавить заметку\n"
      "read - считать заметки\n"
      "read note - прочитать заметку\n"
      "change - изменить заметку\n"
      "del - удалить заметку\n"
      "q - выход")

param = input("Что требуется сделать: ")

while param.lower() != "q":
    if param.lower() == "add":
        add_note()

    elif param.lower() == "read":
        print("Найдены следующие заметки:")
        for note in read_notes.read_dir():
            print(note)

    elif param.lower() == "read note":
        file = input("Какую заметку нужно прочитать: ")
        read_notes.read_note(file)

    elif param.lower() == "change":
        file = input("Какую заметку нужно изменить: ")
        change_notes.change_note(file)

    elif param.lower() == "del":
        file = input("Какую заметку нужно удалить: ")
        change_notes.del_note(file)

    param = input("Что требуется сделать: ")
