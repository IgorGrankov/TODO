#!/usr/bin/env python3
"""
Питоновский скрипт, который при запуске без аргументов показывает текущий список задач
С аргументом 'add' запись с порядковым номером  в список задач
С аргументом 'update' + id возвращает текущее значение и предлагает  перезаписать строку
С аргументом 'remove' + id удаляет запись
С аргументом 'done' + id удаляет запись и помещает её в лог
C аргументом 'log' получаем лог
C аргументом 'rmlog' лог очищаем
В конце каждого вызова отображается последняя версия списка

"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--add')
parser.add_argument('--update')
parser.add_argument('--remove')
parser.add_argument('--done')
parser.add_argument('--log')
parser.add_argument('--rmlog')
args = vars(parser.parse_args())


class Entry(object):
    def __init__(self):
        pass

    def create_entry(self):
        """
        Создаем новую запись 
        Генерируем для нее id
        Возвращаем список
        """
        pass


    def modify_entry(self):
        """
        Модифицируем запись по ключу-id
        Возвращаем список
        """
        pass

    def delete_entry(self):
        """
        При удалении записи надо не забывать обновлять все айдишники
        Возвращаем обновленный лист
        """
        pass

    def mark_as_done(self):
        """
        Копируем запись в лог
        Удаляем запись из списка
        Обновляем айдишники
        """
        pass

    def show_list(self):
        """
        Копируем запись в лог
        Удаляем запись из списка
        Обновляем айдишники
        """
        pass


class Log(object):
    def __init__(self):
        pass

    def show_log(self):
        pass

    def clear_log(self):
        pass


if __name__ == "__main__":
    start = Entry()
    log = Log()

    if args['add']:
        start.create_enrty()
    elif args['update']:
        start.modify_entry()
    elif args['remove']:
        start.delete_entry()
    elif args['done']:
        start.mark_as_done()
    elif args['log']:
        log.show_log()
    elif args['rmlog']:
        log.clear_log()
    else:
        start.show_list()
