class ShortInputException(Exception):
    """Users class of exception"""
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length=length
        self.atleast=atleast

try:
    text=input('Enter something: ')
    if len(text) < 3:
        raise ShortInputException(len(text),3)
except EOFError:
    print('Why do you make EOF')
except ShortInputException as ex:
    print(f"ShortInputException: The length of string is {ex.length}, but should minimum {ex.atleast}")
else:
    print('No was exceptions')
