import os
from pathlib import Path
import uuid

def file_cp1251_utf8(filename):
    """Изменение кодировки файла filename cp1251 -> utf8
        сохранаю в тот же файл.
        использую модуль uuid для генерации имени временного файла
    """
    block_size = 1048576
    filename_utf8 = str(Path(filename).with_name(Path(filename).stem + '.utf.csv'))
    filename_tmp = os.path.join(str(Path(filename).parent.absolute()), str(uuid.uuid4().hex) + '.tmp')
    os.replace(filename, filename_tmp)
    with open(filename_tmp, 'r', encoding='cp1251') as f_source:
        with open(filename, 'w', encoding='utf-8') as f_target:
            while True:
                contents = f_source.read(block_size)
                if not contents:
                    break
                f_target.write(contents)
    os.remove(filename_tmp)
    return filename_utf8
