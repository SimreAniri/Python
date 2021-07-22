"""
 Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
|--my_project
   |--settings
   |  |--__init__.py
   |  |--dev.py
   |  |--prod.py
   |--mainapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--mainapp
   |        |--base.html
   |        |--index.html
   |--authapp
   |  |--__init__.py
   |  |--models.py
   |  |--views.py
   |  |--templates
   |     |--authapp
   |        |--base.html
   |        |--index.html
Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?
"""
# dict_ = {"my_project": [{"settings": ['__init__.py', 'dev.py', 'prod.py']},
#                         {"mainapp": ['__init__.py', 'models.py', 'views.py', {'templates': [{'mainapp': ['base.html', 'index.html']}]}]},
#                         {"authapp": ['__init__.py', 'models.py', 'views.py', {'templates': [{'authapp': ['base.html', 'index.html']}]}]}]}
#
# with open('config.json', 'w', encoding='utf-8') as f:
#     json.dump(dict_, f, indent=4)


import json
import os
import sys


def scan_conf(your_conf, cur_dir=os.path.dirname(__file__)):

    for dir_name in your_conf:
        os.mkdir(os.path.join(cur_dir, dir_name))

        if not your_conf[dir_name]:
            continue

        new_path = os.path.join(cur_dir, dir_name)

        for el in your_conf[dir_name]:
            if type(el) is dict:
                scan_conf(el, new_path)

            else:
                with open(os.path.join(new_path, el), 'w', encoding='utf-8'):
                    pass


with open('config.json', 'r', encoding='utf-8') as f:
    conf = json.load(f)

if os.path.isdir(str(list(conf.keys())[0])):
    print('Такая папка проекта уже существует. Проверьте и запустите скрипт заново.')
    sys.exit(1)

scan_conf(conf)
print('Каталог проекта создан.')
