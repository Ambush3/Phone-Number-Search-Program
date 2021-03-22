import re
phoneNumRegex = re.compile(r'\d\d\d=\d\d\d-\d\d\d\d')
phoneNumRegex.search('My number is 415-555-4242')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group()

phoneNumRegex = re.compile(r'\d\d\d=\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242')
mo.group()

mo.group(1)

mo.group(2)




