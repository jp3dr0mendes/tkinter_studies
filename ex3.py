'''
Exemplo de criação de uma aplicação via oop, com uma classe aplication e controle das funções por meio de métodos 
e atributos
'''

from tkinter import *
from ex1 import test_function

class Application(): #criando a classe
    def __init__(self):
        self.root=Tk() #criando uma janela, atribuindo o Tk() ao atributo root da aplicação
        self.root.mainloop() #chamando no método construtor a função de exibição da janela
    
Application()
test_function()