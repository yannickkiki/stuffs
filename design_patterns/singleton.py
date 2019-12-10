class Ceo():
    is_existing = False
    
    def __init__(self, name):
        if not Ceo.is_existing:
            self.name = name
            Ceo.is_existing = True
        else:
            raise Exception("CEO is a singleton class")


if __name__ == '__main__':
    a = Ceo('Yan')
    b = Ceo('Nasser')
