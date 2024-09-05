a = {}
b = {'Django': 1, 'Node.js': 2, 'R': 3}
c = {
    'uid': 105,
    'login': 'Lara',
    'name': 'Cera Lara Avila',
}

u = c['uid']
c['shell'] = '/bin/zsh'
if c.has_key('login'):
    d = c['login']
else:
    d = None

print d

# Lo mismo, pero mas compacto
# d = c.get('login', None)
