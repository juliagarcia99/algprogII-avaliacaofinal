from node import Node
from livro import Livro
from autor import Autor

class Pilha:
    def __init__(self):
        self.top = None
        self._size = 0


    def push(self, elem):
        #serve p inserir elemento
        node = Node(elem)
        node.next = self.top
        self.top = node
        self.size = self.size + 1

    def pop(self):
        #remove o elemento no topo da pilha
        if self._size > 0:
            node = self.top
            self.top = self.top.next
            self.size = self.size - 1
            return node
        raise IndexError("pilha vazia")


dostoievsky = Autor("1","fyodor dostoievsky")
tolstoy = Autor("2","liev tolstoy")


crimeecastigo = Livro("1","crime e castigo",dostoievsky)
guerraepaz = Livro("2","guerra e paz",tolstoy)
