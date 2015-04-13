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
import os.path


class Entry():
    def __init__(self, entry):
        self.entry = entry

    def create_entry(self):
        """
        Создаем новую запись 
        Генерируем для нее id
        Возвращаем список
        """

        if os.path.isfile('todo_list.dat'):
            notes_file = open('todo_list.dat', 'r')
            lst = notes_file.readlines()
            last_line = lst[len(lst)-1]
            prev_number = last_line.split(':')
            element = prev_number[0]
            num_raw = int(element[1:].replace("'", "", 2)) + 1
            num = str(num_raw)
            notes_file.close()
            notes_file = open('todo_list.dat', 'a')
            entry_row_raw = str(dict.fromkeys(num, row)) + '\n'
            entry_row = entry_row_raw
            notes_file.write(entry_row)
            notes_file.close()
        else:
            notes_file = open('todo_list.dat', 'w+')
            num = '1'
            entry_row_raw = str(dict.fromkeys(num, row)) + '\n'
            entry_row = entry_row_raw
            notes_file.write(entry_row)
            notes_file.close()

        self.show_list()
        return


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
        notes_file = open('todo_list.dat')
        lines = notes_file.readlines()
        for line in lines:
            list_content = line[1:].replace('}', '')
            print(list_content, end='\r')
        return


class Log(object):
    def __init__(self):
        pass

    def show_log(self):
        pass

    def clear_log(self):
        pass


if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument('command', nargs='?')
        parser.add_argument('entry', nargs='?')
        args = parser.parse_args()
        row = args.entry

        entry_list = Entry(row)

        if args.command == 'add':
            entry_list.create_entry()
        elif args.command == 'update':
            entry_list.modify_entry()
        elif args.command == 'remove':
            entry_list.delete_entry()
        elif args.command == 'done':
            entry_list.mark_as_done()
        elif args.command == 'log':
            show_log()
        elif args.command == 'rmlog':
            clear_log()
        else:
            entry_list.show_list()
