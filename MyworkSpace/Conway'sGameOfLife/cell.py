from operator import truediv


class cell:

    def __init__(self):
        self.status = 'dead'

    def alive(self):
        self.status = 'alive'

    def dead(self):
        self.status = 'dead'

    def checker(self): 
        if self.status == 'alive':
            return True
        return False

    def cell_printer(self):
        if self.status == 'alive':
            return '@'
        return '_'


