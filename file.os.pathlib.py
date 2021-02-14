#!/usr/bin/env python

import os
from pathlib import Path


def printheader():
    print('''Content-type:text/html;text/html; charset=utf-8

<html>
<title>Hello world!</title>
<head>
<meta content="text/html;charset=utf-8" http-equiv="Content-Type">
<meta content="utf-8" http-equiv="encoding">
<title>Test</title>
</head>
<body>
''')


def printfooter():
    print('''
</body>
</html>
''')


printheader()


def pr(descr, result):
    print(f'{descr}: <b>{result}</b></br>')

pr('__file__', __file__)
pr('Path(__file__).absolute()', Path(__file__).absolute())
pr('Path(__file__).name', Path(__file__).name)
pr('Path(__file__).stem', Path(__file__).stem)
pr('Path(__file__).suffix', Path(__file__).suffix)
pr('Path(__file__).parent.absolute()', Path(__file__).parent.absolute())
pr('Path(__file__).parts', Path(__file__).parts)
pr('Path(__file__).home()', Path(__file__).home())
pr('Path(__file__).root', Path(__file__).root)
pr('Path("pictures/96e4cdf3fdcc5909796cf7ea99a0db14.text.jpg").absolute()', str(Path('pictures/96e4cdf3fdcc5909796cf7ea99a0db14.text.jpg').absolute()))
pr('Path("pictures/96e4cdf3fdcc5909796cf7ea99a0db14.text.jpg").parent', str(Path('pictures/96e4cdf3fdcc5909796cf7ea99a0db14.text.jpg').parent))
pr('Path("pictures/96e4cdf3fdcc5909796cf7ea99a0db14.text.jpg").parent.absolute()', str(Path('pictures/96e4cdf3fdcc5909796cf7ea99a0db14.text.jpg').parent.absolute()))
pr('Path('').absolute()', str(Path('').absolute()))

print('</br>')
for param in os.environ.keys():
    print(f'<b>{param}</b>: {param, os.environ[param]}</br>')

printfooter()
