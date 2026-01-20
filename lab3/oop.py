"""
ООП реализация сериализации объектов Person с записью в файл.

СПОСОБ 1 нарушение инкапсуляции:
- Прямой доступ к приватным атрибутам
- ПРОБЛЕМЫ: нарушает принципы ООП, код ломается при изменении класса,
  зависит от внутренней реализации

СПОСОБ 2 с инкапсуляцией:
- Использование методов класса для сериализации
- ПРОБЛЕМЫ: требует изменения исходного класса, добавляет временные атрибуты,
  не подходит для сторонних классов
"""

import json
import datetime as dt
from typing import Dict, List, Any


class Person:
    def __init__(self, name: str, born_in: dt.datetime):
        self._name = name
        self._born_in = born_in
        self._friends: List['Person'] = []

    def add_friend(self, friend: 'Person') -> None:
        """Добавляет взаимную дружбу."""
        self._friends.append(friend)
        friend._friends.append(self)


# Способ 1: Нарушение инкапсуляции
def save1(obj: Person, file: str) -> None:
    """Сохраняет объект с прямым доступом к приватным атрибутам."""
    data = _collect1(obj)
    with open(file, 'w') as f:
        json.dump(data, f)


def load1(file: str) -> Person:
    """Загружает объект, создавая без конструктора."""
    with open(file, 'r') as f:
        data = json.load(f)
    return _restore1(data)


def _collect1(obj: Person) -> Dict:
    """Собирает данные объекта."""
    cache = {}

    def collect(obj):
        obj_id = id(obj)
        if obj_id in cache:
            return cache[obj_id]

        d = {
            'id': obj_id,
            'name': obj._name,
            'born_in': obj._born_in.isoformat(),
            'friends': []
        }
        cache[obj_id] = d

        for f in obj._friends:
            fd = collect(f)
            d['friends'].append(fd['id'])

        return d

    root = collect(obj)
    return {'root': root['id'], 'cache': list(cache.values())}


def _restore1(data: Dict) -> Person:
    """Восстанавливает объект из данных."""
    cache = {}

    # Создаем объекты
    for d in data['cache']:
        obj = Person.__new__(Person)
        obj._name = d['name']
        obj._born_in = dt.datetime.fromisoformat(d['born_in'])
        obj._friends = []
        cache[d['id']] = obj

    # Восстанавливаем связи
    for d in data['cache']:
        obj = cache[d['id']]
        for fid in d['friends']:
            obj._friends.append(cache[fid])

    return cache[data['root']]


# Способ 2: С методами класса
class Person2(Person):
    def __init__(self, name: str, born_in: dt.datetime):
        super().__init__(name, born_in)
        self._id = str(id(self))

    def to_dict(self) -> Dict:
        """Возвращает словарь с данными."""
        return {
            'id': self._id,
            'name': self._name,
            'born_in': self._born_in.isoformat(),
            'friends': [f._id for f in self._friends]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Person2':
        """Создает объект из словаря."""
        obj = cls.__new__(cls)
        obj._name = data['name']
        obj._born_in = dt.datetime.fromisoformat(data['born_in'])
        obj._id = data['id']
        obj._friends = []
        obj._fids = data['friends']  # временно храним ID друзей
        return obj


def save2(obj: Person2, file: str) -> None:
    """Сохраняет объект через методы класса."""
    cache = {}

    def collect(obj):
        if obj._id in cache:
            return

        cache[obj._id] = obj.to_dict()
        for f in obj._friends:
            collect(f)

    collect(obj)

    data = {'root': obj._id, 'cache': list(cache.values())}
    with open(file, 'w') as f:
        json.dump(data, f)


def load2(file: str) -> Person2:
    """Загружает объект через методы класса."""
    with open(file, 'r') as f:
        data = json.load(f)

    cache = {}

    # Создаем объекты
    for d in data['cache']:
        obj = Person2.from_dict(d)
        cache[obj._id] = obj

    # Восстанавливаем связи
    for obj in cache.values():
        obj._friends = [cache[fid] for fid in obj._fids]
        del obj._fids

    return cache[data['root']]


def test():
    print("Тест 1 - Способ 1:")
    a = Person("Иван", dt.datetime(2020, 4, 12))
    b = Person("Петр", dt.datetime(2021, 9, 27))
    a.add_friend(b)  # взаимная дружба

    save1(a, 'test1.json')
    a2 = load1('test1.json')

    print(f"Имя: {a2._name}")
    print(f"Друзей: {len(a2._friends)}")
    if a2._friends:
        print(f"Друг: {a2._friends[0]._name}")

    print("\nТест 2 - Способ 2:")
    c = Person2("Анна", dt.datetime(2019, 5, 10))
    d = Person2("Сергей", dt.datetime(2020, 3, 15))
    c.add_friend(d)

    save2(c, 'test2.json')
    c2 = load2('test2.json')

    print(f"Имя: {c2._name}")
    print(f"Друзей: {len(c2._friends)}")
    if c2._friends:
        print(f"Друг: {c2._friends[0]._name}")


if __name__ == "__main__":
    test()