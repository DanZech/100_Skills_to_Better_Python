# code from the book
'''
class Person:
    name = "Person"
    def __init__(self, name = None):
        self.name = name

jon = Person("Jon")
print("%S name is%S" % (Person name, jon.name))
anderson = Person()
anderson.name = "Anderson"
print("%S name is %S" % (Person.name, anderson.name))
'''


#GPT correection
class Person:
    name = "Person"
    def __init__(self, name=None):
        self.name = name

jon = Person("Jon")
print("%s's name is %s" % (Person.name, jon.name))

anderson = Person()
anderson.name = "Anderson"
print("%s's name is %s" % (Person.name, anderson.name))

'''
Este código define uma classe Person com um atributo de classe name e 
um método construtor __init__ que define o nome da pessoa.

O código cria duas instâncias da classe Person. 

A primeira instância é criada com o nome "Jon" passado como argumento para o construtor. 
A segunda instância é criada sem nenhum argumento e, em seguida, seu nome é definido como "Anderson".

O código imprime o nome de cada pessoa usando uma string de formatação que usa o operador %. 
A primeira string de formatação imprime o nome de Person e o nome da primeira pessoa. 
A segunda string de formatação imprime o nome de Person e o nome da segunda pessoa.
'''