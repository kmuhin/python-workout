from decorator_timing import timing
import re


def del_multi_spaces(text):
    return delete_spaces_split(text)

@timing
def delete_spaces_split(text):
    return ' '.join(text.split())

@timing
def delete_spaces_re(text):
    return re.sub('\s{2,}',' ',text).strip()

@timing
def delete_spaces_while(text):
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

if __name__ == '__main__':
    text = ' 17с406-ШР \t 49*70 Полотенце  "Лесная фантазия-1"      цв 1 \n line2 ZZ '	
    print(text)
    print(delete_spaces_split(text))
    print(delete_spaces_re(text))
    print(delete_spaces_while(text))
