def B(fun):
    def add(x, y):
        print('Decorated')
        print(fun(x, y))
    return add


@B
def A(x, y):
    return x+y


docker rmi id/name

A(5, 3)
