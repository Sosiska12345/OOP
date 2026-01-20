"""
Функциональная реализация сериализации объектов Person.

ОТЛИЧИЯ ОТ ООП:
- Нет классов, только структуры данных (словари)
- Нет методов, только функции
- Состояние передается явно между функциями
- Нет инкапсуляции - все данные открыты

ПРОБЛЕМЫ:
- Нет проверки типов на уровне языка
- Легко допустить ошибку в структуре данных
- Нет наследования и полиморфизма
- Сложнее управлять сложными состояниями
"""

import json
import datetime as dt
from typing import Dict, List, Any


def create_person(name: str, born_in: dt.datetime) -> Dict[str, Any]:
    """Создает запись о человеке."""
    return {
        'name': name,
        'born_in': born_in,
        'friends': [],
        'id': str(id({'temp': name}))  # простой уникальный ID
    }


def add_friend(person1: Dict[str, Any], person2: Dict[str, Any]) -> None:
    """Добавляет взаимную дружбу."""
    if person2 not in person1['friends']:
        person1['friends'].append(person2)
    if person1 not in person2['friends']:
        person2['friends'].append(person1)


def save(person: Dict[str, Any], file: str) -> None:
    """Сохраняет объект в файл."""
    data = collect_data(person)
    with open(file, 'w') as f:
        json.dump(data, f)


def load(file: str) -> Dict[str, Any]:
    """Загружает объект из файла."""
    with open(file, 'r') as f:
        data = json.load(f)
    return restore_data(data)


def collect_data(person: Dict[str, Any]) -> Dict[str, Any]:
    """Собирает данные объекта."""
    cache = {}

    def collect(p):
        pid = p['id']
        if pid in cache:
            return cache[pid]

        d = {
            'id': pid,
            'name': p['name'],
            'born_in': p['born_in'].isoformat(),
            'friends': []
        }
        cache[pid] = d

        for f in p['friends']:
            fd = collect(f)
            d['friends'].append(fd['id'])

        return d

    root = collect(person)
    return {'root': root['id'], 'cache': list(cache.values())}


def restore_data(data: Dict[str, Any]) -> Dict[str, Any]:
    """Восстанавливает объект из данных."""
    cache = {}

    # Создаем записи
    for d in data['cache']:
        p = {
            'name': d['name'],
            'born_in': dt.datetime.fromisoformat(d['born_in']),
            'friends': [],
            'id': d['id']
        }
        cache[d['id']] = p

    # Восстанавливаем связи
    for d in data['cache']:
        p = cache[d['id']]
        for fid in d['friends']:
            p['friends'].append(cache[fid])

    return cache[data['root']]


def test():
    print("Тест функционального подхода:")

    a = create_person("Иван", dt.datetime(2020, 4, 12))
    b = create_person("Петр", dt.datetime(2021, 9, 27))
    add_friend(a, b)

    save(a, 'test_fp.json')
    a2 = load('test_fp.json')

    print(f"Имя: {a2['name']}")
    print(f"Друзей: {len(a2['friends'])}")
    if a2['friends']:
        print(f"Друг: {a2['friends'][0]['name']}")


if __name__ == "__main__":
    test()