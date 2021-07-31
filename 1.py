"""
Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера nginx_logs.txt
(https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
— получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:

('141.138.90.60', 'GET', '/downloads/product_2'),
('141.138.90.60', 'GET', '/downloads/product_2'),
('173.255.199.22', 'GET', '/downloads/product_2'),
...

Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
размер которых превышает объем ОЗУ компьютера.
"""

import requests
from collections import Counter


url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
res = requests.get(url, stream=True)

with open('nginx_logs.txt', 'w') as f:
    for chunk in res.iter_content(chunk_size=10000):
        f.write(chunk.decode(encoding=res.encoding))

res_count = Counter()
res_list = []

with open('nginx_logs.txt', 'r') as f:

    for row in f:
        row = row.split()

        if row[0] not in res_count:
            res_count[row[0]] = 0

        res_count[row[0]] += 1
        res_list.append((row[0], row[5][1:], row[6]))

print(res_count.most_common(1))
print(f'Спамер {res_count.most_common(1)[0][0]}: сделал {res_count.most_common(1)[0][1]} запросов')