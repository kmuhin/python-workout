import os
import re

def file_replace_text_input(filename):
    """Замена текста построчно через input output. Сохранение измененеий в тот же файл.
    Есть проблема с кодировкой."""
    list_replace = [('&quot ', '"'), (' +', ' ')]
    with fileinput.FileInput(filename, inplace=True, backup='.bak', mode='U') as file:
        for line in file:
            for i in list_replace:
                line = re.sub(i[0], i[1], u'line')
            print(line, end='')


def file_replace_text(filename, encoding='utf-8'):
    """
    Замена текста в файле с использованием временного файла.
    Открываю стандартным open. Сохраняю изменения в файл с тем же именем.
    Сначала переименовываю filename в filename.bak.
    Открываю filename.bak на чтение и filename на запись.
    """
    list_replace = [('&quot ', '"'), (' +', ' ')]
    os.replace(filename, filename + '.bak', )
    with open(filename + '.bak', 'r', encoding=encoding) as file:
        with open(filename, 'w', encoding=encoding) as file_new:
            for line in file:
                for i in list_replace:
                    line = re.sub(i[0], i[1], line)
                file_new.write(line)
