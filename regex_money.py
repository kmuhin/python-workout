# regex price with thousand separator
# https://www.oreilly.com/library/view/regular-expressions-cookbook/9781449327453/ch06s11.html
# [0-9]{1,3}( [0-9]{3})*(,[0-9]{1,2})?
#            ^ thsep     ^ period
import re

price = 'Цена: 1 122 189,65 р.'
match = re.search('[0-9]{1,3}( [0-9]{3})*(,[0-9]{1,2})?', price)
match.group()
# Out: '1 122 189,65'
