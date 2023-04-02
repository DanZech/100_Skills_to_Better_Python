class InputOutString(object):
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input()
    def printString(self):
        l = self.s.upper()
        print(l)

strObj = InputOutString()
strObj.getString()
strObj.printString()

'''This code defines a class InputOutString with two methods: getString and printString. 
When an instance of this class is created, 
the __init__ method initializes an empty string self.s. 
The getString method reads a string from the user and assigns it to self.s. 
The printString method prints the uppercase version of self.s. 
Finally, the code creates an instance of InputOutString, 
calls getString to read a string from the user, 
and then calls printString to print the uppercase version of the string.'''

'''
Uma classe é uma estrutura de programação orientada a objetos que define um conjunto de atributos 
(variáveis) e métodos (funções) que operam nesses atributos. 
A classe é um modelo que define as características e o comportamento de um objeto.

Em outras palavras, uma classe é como uma planta ou um molde que define como um objeto
deve ser construído e como ele deve se comportar. 
Quando você cria um objeto de uma classe, 
ele é chamado de instância dessa classe e herda as características 
e comportamentos definidos pela classe.

As classes permitem que você organize seu código de forma mais eficiente, 
tornando-o mais legível e fácil de manter. 

Elas são muito úteis em programas grandes e complexos que requerem 
muitos objetos interagindo uns com os outros.

Em Python, você define uma classe usando a palavra-chave "class" 
seguida pelo nome da classe, e em seguida define os atributos 
e métodos da classe dentro de um bloco de código indentado. 

Quando você cria uma instância de uma classe, 
você usa o nome da classe seguido por parênteses, 
como se estivesse chamando uma função.

'''