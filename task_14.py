class American(object):
    pass

class NewYorker(American):
    pass

anAmerican = American()
aNewYorker = NewYorker()
print(anAmerican)
print(aNewYorker)

'''
Este é um programa em Python que define duas classes: 
American e NewYorker. 

NewYorker é uma subclasse de American, 
o que significa que herda todas as propriedades e métodos da classe American.

O programa então cria uma instância de cada classe 
(anAmerican e aNewYorker) usando o método construtor (__init__()) de cada classe. 

Finalmente, o programa imprime a localização de memória de cada objeto usando a função print().

Como as classes American e NewYorker não possuem nenhuma propriedade ou método definido, 
a saída do programa será simplesmente a localização de memória dos objetos, 
que será diferente para cada instância.
'''