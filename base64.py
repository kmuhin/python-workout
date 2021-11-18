import base64


def str_base32(s: str) -> str:
    """
    кодировка строки ascii в base32 в виде строки
    @param s: строка для кодировки ascii
    @return: base32 str
    """
    b32_bytes = base64.b32encode(s.encode('ascii'))
    return b32_bytes.decode('ascii')


def str_base64(s: str) ->:
    b64_bytes = base64.b64encode(s.encode('ascii'))
    return b64_bytes.decode('ascii')


def test_base64(lines):
    for i in lines:
        print('b32'.rjust(10), base64.b32encode(i.encode()))
        print('b64'.rjust(10), base64.b64encode(i.encode()))
        print('urlsafe'.rjust(10), base64.urlsafe_b64encode(i.encode()))
        print('a85'.rjust(10), base64.a85encode(i.encode()))

