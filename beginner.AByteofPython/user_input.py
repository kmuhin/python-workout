from typing import Tuple

forbidden: Tuple[str, str, str] = (".", "?", " ")


def reverse(text):
    return text[::-1]


def is_palindrome(text):
    # version 1
    #for char in forbidden:
    #   text = text.replace(char,'')
    #text = text.upper()
    # version 2
    text = text.translate({ord(i): None for i in forbidden}).upper()
    return text == reverse(text)


something = input('Введите текст: ')

if (is_palindrome(something)):
    print("Да, это палиндром")
else:
    print("Нет, это не палиндром")
