import re

user_input = 'gjrjr@mail.com'

compile = re.compile(r'(SELECT|INSERT|UPDATE|DELETE|WHERE|HAVING|ORDER|BY|LIMIT)')
if re.match(compile, user_input.upper()):
    print('sql')

if re.search(r'(\'|;|\")', user_input):
    print('!!!!!!!')