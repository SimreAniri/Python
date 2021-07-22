"""
Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
Написать скрипт, который собирает все шаблоны в одну папку templates, например:
|--my_project
   ...
  |--templates
   |   |--mainapp
   |   |  |--base.html
   |   |  |--index.html
   |   |--authapp
   |      |--base.html
   |      |--index.html
Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
(они играют роль пространств имён);
предусмотреть возможные исключительные ситуации;
"""
import os

"""
Как я не вчитываюсь в задание, но в упор не могу понять, что от меня требуется.
Было бы неплохо предоставить структуру в формате было-стало...
Надеюсь, поняла смысл задания верно.
"""

ROOT_DIR = 'G:\Программирование\_Разработчик Python\I четверть\Основы языка Python\Python\my_project'

for root, dirs, files in os.walk(ROOT_DIR):

    if os.path.basename(root) == 'templates' and os.path.dirname(root) != ROOT_DIR:
        new_temp = os.path.join(ROOT_DIR, 'templates')

        if not os.path.exists(os.path.join(ROOT_DIR, 'templates')):
            os.mkdir(new_temp)

        for el in os.scandir(root):
            os.rename(el.path, os.path.join(new_temp, el.name))

        os.rmdir(root)

print('Перемещения закончены.')
