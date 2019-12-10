from abc import ABC, abstractmethod


class T(ABC):

    @abstractmethod
    def do_this(self):
        pass


if __name__ == '__main__':
    t = T()
