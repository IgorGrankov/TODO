#!/usr/bin/env python3
"""
Питоновский скрипт, который при запуске без аргументов показывает текущий список задач
С аргументом 'add' запись с порядковым номером  в список задач
С аргументом 'update' + id возвращает текущее значение и предлагает  перезаписать строку
С аргументом 'del' + id удаляет запись
С аргументом 'done' + id удаляет запись и помещает её в лог
C аргументом 'log' получаем лог
C аргументом 'clear' лог очищаем
C аргументом 'help' выводим содержимое данного докстринга
В конце каждого вызова отображается последняя версия списка

"""
import kwargs


class List(object): 
   def __init__(self, list_of_entries, last_modified):
       self.list_of_entries = list_of_entries
       self.last_modified = last_modified
       
   def show_list():
       self.list_of_entries = {}
       print()
      

class Entry(object):
    def __init__(self, id, entry):
        self.id = id
        self.entry = entry

    def create_entry():
        """
        Создаем новую запись 
        Генерируем для нее id
        Возвращаем список
        """
        pass

    def modify_entry():
        """
        Модифицируем запись по ключу-id
        Возвращаем список
        """
        pass

    def delete_entry():
        """
        При удалении записи надо не забывать обновлять все айдишники
        Возвращаем обновленный лист
        """
        pass

    def mark_as_done():
        """
        Копируем запись в лог
        Удаляем запись из списка
        Обновляем айдишники
        """
        pass


class Log(object):
   def __init__(self):
       pass

   def show_log():
       pass

   def clear_log():
       pass

if name == "__main__":
   start = List()
   start.show_list()
