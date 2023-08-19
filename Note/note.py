from datetime import datetime
import json


class Note:
    __count_note = 0
    __new = True

    def __init__(self, name="", text=""):
        Note.__count_note += 1
        self.__name = name
        self.text = text
        self.__id = datetime.now().strftime("%m%d%H%M%S") + str(Note.__count_note)
        self.__data = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.__file = f"{self.__id}_{self.__name}.json"

    def print_note(self):
        return f"{self.__id} {self.__name} {self.__data}\n{self.text}"

    def get_file_name(self):
        return self.__file

    def get_data(self):
        return datetime.strptime(self.__data, "%Y-%m-%d %H:%M")

    def change_name(self, name):
        self.__name = name
        self.__file = f"{self.__id}_{self.__name}.json"
        self.__new = True

    def save_json(self):
        data = {"name": self.__name,
                "text": self.text,
                "id": self.__id,
                "data": self.__data}

        if self.__new:
            with open(self.__file, "w") as f:
                json.dump(data, f, sort_keys=True)

        else:
            print("Вы хотите сохранить изменения в текущем файле?")
            print("Y/N")
            if input().upper() == "Y":
                with open(self.__file, "w") as f:
                    json.dump(data, f, sort_keys=True)

            else:
                print("Создать новый файл?")
                print("Y/N")
                if input().upper() == "Y":
                    file = f"{datetime.now().strftime('%m%d%H%M%S') + str(Note.__count_note)}_{self.__name}.json"
                    with open(file, "w") as f:
                        json.dump(data, f, sort_keys=True)
                    print(f"{file} создан")
                    self.__file = file

                else:
                    print("Запись отменена")
                    return False
        return True

    def read_json(self, file):
        flag = False
        try:
            with open(file, "r") as f:
                data = json.load(f)
                self.__name = data["name"]
                self.text = data["text"]
                self.__id = data["id"]
                self.__data = data["data"]
                self.__new = False
                self.__file = file
        except KeyError:
            print("Неверный формат файла")
        except FileNotFoundError:
            print("Файл не найден")
        else:
            flag = True

        return flag
