# arbitary argument
# *arg
# arbitary keyword argument
# **kwarg


def new (*arg):
    print(arg)
new(10,2,3,4,5)

name=lambda *arg:arg+arg
print(name)