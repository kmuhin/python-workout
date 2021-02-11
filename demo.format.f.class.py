#!/usr/bin/env python

col1=''
print(
    f"{'test':>10}"
    f"{'test':>10}"
    f"{1:010d}"
)


from string import Template
t = Template('Hey, $name!')
name="Bob"
print(t.substitute(name=name))

class Demo:  # Python 3
    
    def __str__(self):
        return 'str'
    
    def __repr__(self):
        return 'repr'
    
    def __ascii__(self):
        return 'ascii'
    
    def __format__(self, format_spec):
        return 'format'

demo=Demo()
print('{!s}-{!r}-{!a}-{}'.format(demo,demo,demo,demo))