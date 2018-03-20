import itertools

class Chainable(object):
    def __init__(self):
        self.data = {}
        pass

    def process(self):
        pass

    def emit(self):
        pass


def node_a(Chainable):
    def process(self):
        self.data['x'] += 10
        return self

def node_b(Chainable):
    def process(self):
        self.data['x'] += 12
        return self

def genz(z):
    for out in range(z):
        yield(z)


if __name__ == '__main__':
    z = genz(5).node_a().node_b()

    print z
