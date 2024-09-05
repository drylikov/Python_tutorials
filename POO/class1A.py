class C1(object):
    x = 23

print C1.x
print C1.__name__, C1.__bases__

C1.y = 45
#C1.__dict__['z'] = 48
print C1.x, C1.y
